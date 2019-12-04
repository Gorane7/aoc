min = 138307
max = 654504
possibilities = 0
for i in range(min, max + 1):
    possibility = str(i)
    last = None
    has_double = False
    never_decreases = True
    adjacents = []
    for digit in possibility:
        if last:
            if digit == last:
                adjacents[-1] += 1
            else:
                adjacents.append(1)
            if int(digit) < int(last):
                never_decreases = False
        else:
            adjacents.append(1)
        last = digit
    if never_decreases and 2 in adjacents:
        print(i)
        possibilities += 1
print(possibilities)
