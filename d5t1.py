import aoc

file = open('d5t1i.txt')
program = list(map(int,file.read().strip('\n').split(',')))
file.close()
new_computer = aoc.Computer(program, True)
new_computer.inputs.append(5)
new_computer.run()
print(new_computer.outputs)
