

class Computer():

    def __init__(self, program, automatic=False, pause_when_output=False):
        self.program = program
        self.running = False
        self.count = 0
        self.relative_base = 0
        self.automatic = automatic
        self.inputs = []
        self.outputs = []
        self.pause_when_output = pause_when_output
        self.outputted = False
        self.instructions = {
            1: {
                'params': 3,
                'func': self.add
            },
            2: {
                'params': 3,
                'func': self.multiply
            },
            3: {
                'params': 1,
                'func': self.write_to
            },
            4: {
                'params': 1,
                'func': self.output
            },
            5: {
                'params': 2,
                'func': self.jump_if_true
            },
            6: {
                'params': 2,
                'func': self.jump_if_false
            },
            7: {
                'params': 3,
                'func': self.less_than
            },
            8: {
                'params': 3,
                'func': self.equals
            },
            9: {
                'params': 1,
                'func': self.adjust_relative_base
            },
            99: {
                'params': 0,
                'func': self.exit
            }
        }

    def overwrite_program(self, program):
        self.program = program

    def overwrite_value_in_program(self, pos, value):
        while len(self.program) <= pos:
            self.program.append(0)
        self.program[pos] = value

    def read_value_from_program(self, pos):
        while len(self.program) <= pos:
            self.program.append(0)
        return self.program[pos]

    def run(self):
        self.running = True
        self.outputted = False
        while self.running and (not self.outputted or not self.pause_when_output):
            self.need_to_increase = True
            instruction_base = self.read_value_from_program(self.count)
            #print("")
            #print(instruction_base)
            instruction = instruction_base % 100
            mode_str = str(instruction_base // 100)[::-1]
            #print(instruction)
            if instruction not in self.instructions.keys():
                raise Exception('There is no instruction: ' + str(instruction))
            params = []
            modes = []
            param_amount = self.instructions[instruction]['params']
            for i in range(1, param_amount + 1):
                if len(mode_str) >= i:
                    modes.append(int(mode_str[i-1]))
                else:
                    modes.append(0)
                params.append(self.read_value_from_program(self.count + i))
            #print(str(instruction_base) + " " + str(params))
            self.instructions[instruction]['func'](params, modes)
            if self.need_to_increase:
                self.count += param_amount + 1
            #print(len(self.program))
            #print("")

    def get_values(self, params, modes):
        values = []
        for i in range(len(params)):
            if modes[i] == 0:
                values.append(self.read_value_from_program(params[i]))
            elif modes[i] == 1:
                values.append(params[i])
            elif modes[i] == 2:
                #print(self.relative_base)
                #print(params[i])
                #print(self.read_value_from_program(params[i] + self.relative_base))
                values.append(self.read_value_from_program(params[i] + self.relative_base))
            else:
                raise Exception('There is no mode ' + str(modes[i]))
            #print("Mode " + str(modes[i]))
        return values

    def get_target(self, base, mode):
        if mode == 2:
            return self.relative_base + base
        return base

    def add(self, params, modes):
        x, y = tuple(self.get_values(params[:-1], modes[:-1]))
        target = self.get_target(params[-1], modes[-1])
        self.overwrite_value_in_program(target, x + y)
        print("Added " + str(x) + " and " + str(y) + " and wrote it to location " + str(target))

    def multiply(self, params, modes):
        x, y = tuple(self.get_values(params[:-1], modes[:-1]))
        target = self.get_target(params[-1], modes[-1])
        self.overwrite_value_in_program(target, x * y)
        print("Multiplied " + str(x) + " and " + str(y) + " and wrote it to location " + str(target))

    def write_to(self, params, modes):
        target = self.get_target(params[-1], modes[-1])
        #target = self.get_values(params, modes)[0]
        if self.automatic:
            value = self.inputs[0]
            self.overwrite_value_in_program(target, value)
            self.inputs.pop(0)
            #print(self.inputs)
        else:
            value = int(input("Input needed: "))
            self.overwrite_value_in_program(target, value)
        print("Wrote " + str(value) + " to location " + str(target))

    def output(self, params, modes):
        value = self.get_values(params, modes)[0]
        #print(target)
        if self.automatic:
            self.outputs.append(value)
        else:
            print("Output: " + str(value))
        self.outputted = True

    def jump_if_true(self, params, modes):
        condition, value = self.get_values(params, modes)
        if condition:
            self.need_to_increase = False
            self.count = value
            print("Jumped read head to " + str(value))
        else:
            print("Didn't jump")

    def jump_if_false(self, params, modes):
        condition, value = self.get_values(params, modes)
        if not condition:
            self.need_to_increase = False
            self.count = value
            print("Jumped read head to " + str(value))
        else:
            print("Didn't jump")

    def less_than(self, params, modes):
        x1, x2 = self.get_values(params[:-1], modes[:-1])
        target = self.get_target(params[-1], modes[-1])
        if x1 < x2:
            self.overwrite_value_in_program(target, 1)
            print(str(x1) + " is less than " + str(x2) + " so wrote 1 to location " + str(target))
        else:
            self.overwrite_value_in_program(target, 0)
            print(str(x1) + " is not less than " + str(x2) + " so wrote 0 to location " + str(target))

    def equals(self, params, modes):
        x1, x2 = self.get_values(params[:-1], modes[:-1])
        target = self.get_target(params[-1], modes[-1])
        if x1 == x2:
            self.overwrite_value_in_program(target, 1)
            print(str(x1) + " equals " + str(x2) + " so wrote 1 to location " + str(target))
        else:
            self.overwrite_value_in_program(target, 0)
            print(str(x1) + " does not equal " + str(x2) + " so wrote 0 to location " + str(target))

    def adjust_relative_base(self, params, modes):
        mod = self.get_values(params, modes)[0]
        self.relative_base += mod
        print("Adjusted relative base from " + str(self.relative_base - mod) + " to " + str(self.relative_base))

    def exit(self, params=None, modes=None):
        self.running = False
        print("Exiting")
