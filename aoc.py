

class Computer():

    def __init__(self, program, automatic=False, pause_when_output=False):
        self.program = program
        self.running = False
        self.count = 0
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
            99: {
                'params': 0,
                'func': self.exit
            }
        }

    def overwrite_program(self, program):
        self.program = program

    def overwrite_value_in_program(self, pos, value):
        self.program[pos] = value

    def run(self):
        self.running = True
        self.outputted = False
        while self.running and (not self.outputted or not self.pause_when_output):
            self.need_to_increase = True
            instruction_base = self.program[self.count]
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
                params.append(self.program[self.count + i])
            self.instructions[instruction]['func'](params, modes)
            if self.need_to_increase:
                self.count += param_amount + 1
            #print(self.program, self.count)

    def get_values(self, params, modes):
        values = []
        for i in range(len(params)):
            if modes[i] == 0:
                values.append(self.program[params[i]])
            elif modes[i] == 1:
                values.append(params[i])
            else:
                raise Exception('There is no mode ' + str(modes[i]))
        return values

    def add(self, params, modes):
        x, y = tuple(self.get_values(params[:-1], modes[:-1]))
        target = params[-1]
        self.program[target] = x + y

    def multiply(self, params, modes):
        x, y = tuple(self.get_values(params[:-1], modes[:-1]))
        target = params[-1]
        self.program[target] = x * y

    def write_to(self, params, modes):
        target = params[0]
        if self.automatic:
            self.program[target] = self.inputs[0]
            self.inputs.pop(0)
            #print(self.inputs)
        else:
            self.program[target] = int(input("Input needed: "))

    def output(self, params, modes):
        target = self.get_values(params, modes)[0]
        #print(target)
        if self.automatic:
            self.outputs.append(target)
        else:
            print(target)
        self.outputted = True

    def jump_if_true(self, params, modes):
        condition, value = self.get_values(params, modes)
        if condition:
            self.need_to_increase = False
            self.count = value

    def jump_if_false(self, params, modes):
        condition, value = self.get_values(params, modes)
        if not condition:
            self.need_to_increase = False
            self.count = value

    def less_than(self, params, modes):
        x1, x2 = self.get_values(params[:-1], modes[:-1])
        target = params[-1]
        if x1 < x2:
            self.program[target] = 1
        else:
            self.program[target] = 0

    def equals(self, params, modes):
        x1, x2 = self.get_values(params[:-1], modes[:-1])
        target = params[-1]
        if x1 == x2:
            self.program[target] = 1
        else:
            self.program[target] = 0

    def exit(self, params=None, modes=None):
        self.running = False

def find_recursive_fuel(initial_fuel, new_fuel_function):
    if initial_fuel <= 0:
        return 0
    return initial_fuel + find_recursive_fuel(new_fuel_function(initial_fuel), new_fuel_function)
