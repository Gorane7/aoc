import copy

wire1 = None
wire2 = None
file1 = open('d3w1.txt', 'r')
wire1 = file1.read().strip('\n').split(',')
file1.close()
file2 = open('d3w2.txt', 'r')
wire2 = file2.read().strip('\n').split(',')
file2.close()

for i in range(len(wire1)):
    wire1[i] = [wire1[i][0], int(wire1[i][1:])]
for i in range(len(wire2)):
    wire2[i] = [wire2[i][0], int(wire2[i][1:])]

wire1_locs = []
wire2_locs = []

count = 0
wire1_len = len(wire1)
last_loc = [0, 0]
'''
while True:
    if wire1[count][1] > 0:
        wire1[count][1] -= 1
        if wire1[count][0] == 'U':
            last_loc[0] -= 1
        elif wire1[count][0] == 'D':
            last_loc[0] += 1
        elif wire1[count][0] == 'L':
            last_loc[1] -= 1
        elif wire1[count][0] == 'R':
            last_loc[1] += 1
        wire1_locs.append(copy.copy(last_loc))
    else:
        count += 1
        if count == wire1_len:
            break
'''

count = 0
wire2_len = len(wire2)
last_loc = [0, 0]
'''
while True:
    if wire2[count][1] > 0:
        wire2[count][1] -= 1
        if wire2[count][0] == 'U':
            last_loc[0] -= 1
        elif wire2[count][0] == 'D':
            last_loc[0] += 1
        elif wire2[count][0] == 'L':
            last_loc[1] -= 1
        elif wire2[count][0] == 'R':
            last_loc[1] += 1
        wire2_locs.append(copy.copy(last_loc))
    else:
        count += 1
        if count == wire2_len:
            break
'''

'''
intersections = []
wire1_locs_len = len(wire1_locs)
for i, wire1_loc in enumerate(wire1_locs):
    print(i / wire1_locs_len)
    for wire2_loc in wire2_locs:
        if wire1_loc == wire2_loc:
            intersections.append(copy.copy(wire1_loc))
print(intersections)
'''

intersections = [[0, 308], [0, 876], [-263, 876], [-409, -1111], [249, -1210], [1159, -595], [1159, -376], [1159, -325], [1346, -237], [1572, -237], [1572, 113], [1494, -325], [1075, -3662], [1109, -3686], [1109, -4072], [1099, -3662], [1425, -2763], [1392, -2616], [655, -2590], [655, -2836], [1183, -2325], [1183, -2231], [923, -1894], [753, -2231], [655, -2316], [175, -1769], [92, -1857], [92, -2380], [220, -2685], [655, -2685], [849, -2231], [923, -2176], [1546, -2694], [1392, -2694], [1380, -2325], [1546, -2288], [1354, -969], [1354, -933], [1572, -307], [1346, -307], [905, -307], [705, -307], [683, -719], [683, -1003], [-523, -1753], [-588, -1753], [-864, -2567], [-60, -3022], [220, -3022], [559, -3022], [1572, -269], [1346, -269], [905, -269], [829, -325], [829, -595], [829, -719], [1017, -741], [1354, -741], [1532, -325], [1572, -185], [1126, -595], [1354, -1293], [1871, 2274], [1756, 2114], [1520, 1471], [1823, 1162], [976, 1985], [930, 2309]]
#intersection_lengths = list(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
#print(intersection_lengths)
wire1_steps = []
wire2_steps = []

for intersection in intersections:
    dist = 0
    loc = [0, 0]
    for wire_step in wire1:
        #print(wire_step)
        if wire_step[0] in ['U', 'D']:
            if intersection[1] != loc[1]:
                dist += wire_step[1]
            else:
                if wire_step[0] == 'U':
                    if intersection[0] < loc[0] and intersection[0] >= loc[0] + wire_step[1]:
                        dist += loc[0] - intersection[0]
                        break
                    dist += wire_step[1]
                else:
                    if intersection[0] > loc[0] and intersection[0] <= loc[0] + wire_step[1]:
                        dist += intersection[0] - loc[0]
                        break
                    dist += wire_step[1]
            if wire_step[0] == 'U':
                loc[0] -= wire_step[1]
            else:
                loc[0] += wire_step[1]
        else:
            if intersection[0] != loc[0]:
                dist += wire_step[1]
            else:
                if wire_step[0] == 'R':
                    if intersection[1] > loc[1] and intersection[1] <= loc[1] + wire_step[1]:
                        dist += intersection[1] - loc[1]
                        break
                    dist += wire_step[1]
                else:
                    if intersection[1] < loc[1] and intersection[1] >= loc[1] + wire_step[1]:
                        dist += loc[1] - intersection[1]
                        break
                    dist += wire_step[1]
            if wire_step[0] == 'R':
                loc[1] += wire_step[1]
            else:
                loc[1] -= wire_step[1]
    wire1_steps.append(dist)

for intersection in intersections:
    dist = 0
    loc = [0, 0]
    for wire_step in wire2:
        print(wire_step)
        if wire_step[0] in ['U', 'D']:
            if intersection[1] != loc[1]:
                dist += wire_step[1]
            else:
                if wire_step[0] == 'U':
                    if intersection[0] < loc[0] and intersection[0] >= loc[0] + wire_step[1]:
                        dist += loc[0] - intersection[0]
                        break
                    dist += wire_step[1]
                else:
                    if intersection[0] > loc[0] and intersection[0] <= loc[0] + wire_step[1]:
                        dist += intersection[0] - loc[0]
                        break
                    dist += wire_step[1]
            if wire_step[0] == 'U':
                loc[0] -= wire_step[1]
            else:
                loc[0] += wire_step[1]
        else:
            if intersection[0] != loc[0]:
                dist += wire_step[1]
            else:
                if wire_step[0] == 'R':
                    if intersection[1] > loc[1] and intersection[1] <= loc[1] + wire_step[1]:
                        dist += intersection[1] - loc[1]
                        break
                    dist += wire_step[1]
                else:
                    if intersection[1] < loc[1] and intersection[1] >= loc[1] + wire_step[1]:
                        dist += loc[1] - intersection[1]
                        break
                    dist += wire_step[1]
            if wire_step[0] == 'R':
                loc[1] += wire_step[1]
            else:
                loc[1] -= wire_step[1]
    wire2_steps.append(dist)

#print(intersections)
#print(wire1_steps)
#print(wire2_steps)

sums = []
for i in range(len(wire1_steps)):
    sums.append(wire1_steps[i] + wire2_steps[i])
print(sorted(sums))

print(sum(map(lambda x: x[1], wire1)))
print(sum(map(lambda x: x[1], wire2)))
