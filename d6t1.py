file = open('d6i.txt', 'r')
data = file.readlines()
file.close()
for i in range(len(data)):
    data[i] = data[i].strip('\n').split(')')

class Planet:
    def __init__(self, name, parent):
        self.name = name
        self.orbits = []
        self.parent = parent

    def add_orbits(self, relations):
        to_remove = []
        for i in range(len(relations)):
            if relations[i][0] == self.name:
                to_remove.append(relations[i])
        for object in to_remove:
            relations.remove(object)
            self.orbits.append(Planet(object[1], self))
        for orbit in self.orbits:
            orbit.add_orbits(relations)

    def count_orbits(self, depth):
        total = 0
        for orbit in self.orbits:
            total += orbit.count_orbits(depth + 1)
        return total + depth

    def contains(self, value):
        if self.name == value:
            return True
        for orbit in self.orbits:
            if orbit.contains(value):
                return True
        return False

    def find(self, value):
        if self.name == value:
            return self
        for orbit in self.orbits:
            if orbit.contains(value):
                return orbit.find(value)

    def dist(self, goal, so_far):
        if self.name == goal.name:
            return so_far - 2
        for orbit in self.orbits:
            if orbit.contains(goal.name):
                return orbit.dist(goal, so_far + 1)
        return self.parent.dist(goal, so_far + 1)

com = Planet('COM', None)
com.add_orbits(data)
print(com.find('YOU').dist(com.find('SAN'), 0))
