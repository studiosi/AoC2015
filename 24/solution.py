import itertools

packages = set([ int(l) for l in open("input.txt").readlines() ])

def entanglement(group):
    r = 1
    for i in group:
        r = r * i
    return r

def check(packages,  partsLeft):
    for groupLen in range(1,  len(packages)):
        for group in itertools.combinations(packages,  groupLen):
            packagesLeft = packages - set(group)
            # 2 parts left
            if sum(group) == weight and partsLeft == 2:
                return True
            # more than 2 parts left
            elif sum(group) == weight and partsLeft > parts:
                return check(packagesLeft,  partsLeft - 1)
            # last part
            elif sum(group) == weight and check(packagesLeft,  partsLeft - 1):
                # Return the quantum entanglement
                return entanglement(group)

# Part 1
parts = 3
weight = sum(packages) // parts  
print(check(packages,  parts))

# Part 2
parts = 4
weight = sum(packages) // parts  
print(check(packages,  parts))
