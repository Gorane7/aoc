#Fuel required to launch a given module is based on its mass.
#Specifically, to find the fuel required for a module.
#take its mass
#divide by three
#round down
#subtract 2.
total = 0
with open("d1t1i.txt", "r") as file:
    for line in file.readlines():
        total += (int(line.strip("\n")) // 3) - 2
print(total)
