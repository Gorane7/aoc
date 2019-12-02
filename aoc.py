

class Computer():

    def __init__(self, program):
        self.program = program
        self.running = False
        self.instructions = {
            1: {
                'params': 3,
                'func': self.add
            },
            2: {
                'params': 3,
                'func': self.multiply
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

    def run(self, count=0):
        self.running = True
        while self.running:
            instruction = self.program[count]
            #print(instruction)
            if instruction not in self.instructions.keys():
                raise Exception('There is no instruction: ' + str(instruction))
            params = []
            param_amount = self.instructions[instruction]['params']
            for i in range(1, param_amount + 1):
                params.append(self.program[count + i])
            self.instructions[instruction]['func'](*tuple(params))
            count += param_amount + 1

    def add(self, x, y, target):
        self.program[target] = self.program[x] + self.program[y]

    def multiply(self, x, y, target):
        self.program[target] = self.program[x] * self.program[y]

    def exit(self):
        self.running = False

def find_recursive_fuel(initial_fuel, new_fuel_function):
    if initial_fuel <= 0:
        return 0
    return initial_fuel + find_recursive_fuel(new_fuel_function(initial_fuel), new_fuel_function)
