import aoc

file = open('d5t1i.txt')
program = list(map(int,file.read().strip('\n').split(',')))
file.close()
new_computer = aoc.Computer(program)
new_computer.run()
