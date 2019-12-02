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
    total = cost
    added = total
    while added > 0:
        print(added)
        new = (added // 3) - 2
        #print(new)
        if new > 0:
            total += new
        added = new
    real_costs.append(total)
print(sum(real_costs))
