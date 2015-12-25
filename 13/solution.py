import itertools

def analyseLine(l): 
	x = l.split()
	amount = (int(x[3]) * -1) if (x[2] == 'lose') else int(x[3])
	return(x[0], amount, x[-1].replace('.', ''))

def getPairs(names):
	names = list(names)
	names.append(names[0])
	r = []
	for i in range(len(names) - 1):
		r.append((names[i], names[i+1]))
		r.append((names[i+1], names[i]))
	return r

def getRelations(info):
	r = {}
	for i in info:
		s = i[0] + i[2]
		r[s] = i[1]
	return r

def calculateTotal(pairs, relations):
	r = 0
	for p in pairs:
		r += relations[p[0] + p[1]]
	return r

def calculateTotal_2(pairs, relations):
	r = 0
	for p in pairs:
		if p[0] is not 'ME' and p[1] is not 'ME':
			r += relations[p[0] + p[1]]
	return r

inp = open('input.txt').readlines()

info = [analyseLine(l) for l in inp]
names = set([x[0] for x in info])
relations = getRelations(info)

# PART 1
x = -999999999999999999999999
for perm in itertools.permutations(names):
	pairs = getPairs(perm)
	try:
		r = calculateTotal(pairs, relations)
		if r > x:
			x = r
	except:
		continue
print("PART 1: " + str(x))

# PART 2
names = set([x[0] for x in info])
names.add("ME")
relations = getRelations(info)
x = -999999999999999999999999
for perm in itertools.permutations(names):
	pairs = getPairs(perm)
	try:
		r = calculateTotal_2(pairs, relations)
		if r > x:
			x = r
	except:
		continue
print("PART 2: " + str(x))
	
	