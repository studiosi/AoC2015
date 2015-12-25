import re
import copy
import random

changes = {}
chain = ""
lines = open('input.txt').readlines()
moreChanges = True
for l in lines:
    l = l.strip()
    if moreChanges and l != "":
        x = l.split("=>")
        if x[0].strip() not in changes.keys():
            changes[x[0].strip()] = []
        changes[x[0].strip()].append(x[1].strip())
    elif (not moreChanges) and l != "":
        chain += l
    elif l == "":
        moreChanges = False

# Part 1
c = []
for k in changes.keys():
    p = re.compile(k)   
    for i in changes[k]: 
        for m in p.finditer(chain):
            s = copy.copy(chain)
            s = s[:m.start()] + i + s[m.end():]
            if s not in c:
                c.append(s)
print(len(c))

# Part 2
x = "".join(open('input.txt').readlines())

molecule = chain[::-1]
reps = {m[1][::-1]: m[0][::-1] for m in re.findall(r'(\w+) => (\w+)', x)}
def rep(x):
    return reps[x.group()]
count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1
print(count)