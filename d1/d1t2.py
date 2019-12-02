import aoc

#Fuel required to launch a given module is based on its mass.
#Specifically, to find the fuel required for a module.
#take its mass
#divide by three
#round down
#subtract 2.
#recursively add fuel for the fuel
total = 0
costs = []
with open("d1t1i.txt", "r") as file:
    for line in file.readlines():
        costs.append((int(line.strip("\n")) // 3) - 2)
real_costs = []
for cost in costs:
    real_costs.append(aoc.find_recursive_fuel(cost, lambda x: (x // 3) - 2))
print(sum(real_costs))
