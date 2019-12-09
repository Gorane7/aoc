import copy
import aoc

software = [3,8,1001,8,10,8,105,1,0,0,21,46,55,76,89,106,187,268,349,430,99999,3,9,101,4,9,9,1002,9,2,9,101,5,9,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]

answers = []

for a in range(5, 10):
    for b in range(5, 10):
        for c in range(5, 10):
            for d in range(5, 10):
                for e in range(5, 10):
                    phase_settings = [a, b, c, d, e]

                    if len(phase_settings) != len(list(set(phase_settings))):
                        continue

                    test_soft = software

                    #print(phase_settings)

                    A = aoc.Computer(copy.deepcopy(test_soft), True, True)
                    A.inputs = [a]
                    B = aoc.Computer(copy.deepcopy(test_soft), True, True)
                    B.inputs = [b]
                    C = aoc.Computer(copy.deepcopy(test_soft), True, True)
                    C.inputs = [c]
                    D = aoc.Computer(copy.deepcopy(test_soft), True, True)
                    D.inputs = [d]
                    E = aoc.Computer(copy.deepcopy(test_soft), True, True)
                    E.inputs = [e]

                    io = 0
                    looping = True

                    computers = [A, B, C, D, E]

                    while looping:
                        for computer in computers:
                            computer.inputs.append(io)
                            computer.run()
                            io = computer.outputs[-1]
                            if not computer.running:
                                looping = False
                    answers.append(io)
print(len(answers))
print(answers)
print(max(answers))

"""
test_soft = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phase_settings = [4,3,2,1,0]
this_soft = copy.deepcopy(test_soft)
computer = aoc.Computer(this_soft)
computer.automatic = True
computer.stop_when_output = True
outputs = [0]
for i in range(5):
    computer = aoc.Computer(this_soft)
    computer.automatic = True
    computer.stop_when_output = True
    #print(computer.outputs)
    #print(i)
    this_soft = copy.deepcopy(test_soft)
    computer.program = this_soft
    computer.inputs.append(phase_settings[i])
    computer.inputs.append(outputs[-1])
    #print(computer.program)
    print(computer.inputs)
    computer.run()
    print(computer.outputs[-1])
    outputs.append(computer.outputs[-1])
    print("")
"""


#print(computer.outputs)

print("")
print("!")
print("")

"""
#4, 43, 432, 4321, 43210
test_soft = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
A = aoc.Computer(copy.deepcopy(test_soft))
A.automatic = True
A.inputs = [9]
B = aoc.Computer(copy.deepcopy(test_soft))
B.automatic = True
B.inputs = [7]
C = aoc.Computer(copy.deepcopy(test_soft))
C.automatic = True
C.inputs = [8]
D = aoc.Computer(copy.deepcopy(test_soft))
D.automatic = True
D.inputs = [5]
E = aoc.Computer(copy.deepcopy(test_soft))
E.automatic = True
E.inputs = [6]
io = 0
looping = True
computers = [A, B, C, D, E]
while looping:
    for computer in computers:
        computer.inputs.append(io)
        computer.run()
        io = computer.outputs[-1]
"""
