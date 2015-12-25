import numpy as np

def isNumber(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

def getRequiredSignals(instr):
	x = instr.split()
	r = []
	# AND / OR
	if x[1] == 'AND' or x[1] == 'OR':
		if not isNumber(x[0]):
			r.append(x[0])
		if not isNumber(x[2]):
			r.append(x[2])
	# LSHIFT / RSHIFT
	elif x[1] == 'LSHIFT' or x[1] == 'RSHIFT':
		r.append(x[0])
	# NOT
	elif x[0] == 'NOT':
		r.append(x[1])
	# SIGNAL TO SIGNAL
	elif not isNumber(x[0]):
		r.append(x[0])	
	return r

def checkRequirements(req):
	for r in req:
		if not r in currentSignals.keys():
			return False
	return True

def executeInstruction(instr):
	x = instr.split()
	if x[1] == 'AND': # AND
		if not isNumber(x[0]):
			v1 = currentSignals[x[0]]
		else:
			v1 = np.uint16(x[0])
		if not isNumber(x[2]):
			v2 = currentSignals[x[2]]
		else:
			v1 = np.uint16(x[2])
		currentSignals[x[4]] = np.bitwise_and(v1, v2)
	elif x[1] == 'OR': # OR
		if not isNumber(x[0]):
			v1 = currentSignals[x[0]]
		else:
			v1 = np.uint16(x[0])
		if not isNumber(x[2]):
			v2 = currentSignals[x[2]]
		else:
			v1 = np.uint16(x[2])
		currentSignals[x[4]] = np.bitwise_or(v1, v2)
	elif x[1] == 'LSHIFT': # LSHIFT
		v1 = currentSignals[x[0]]
		v2 = np.uint16(x[2])
		currentSignals[x[4]] = np.left_shift(v1, v2)
	elif x[1] == 'RSHIFT': # RSHIFT
		v1 = currentSignals[x[0]]
		v2 = np.uint16(x[2])
		currentSignals[x[4]] = np.right_shift(v1, v2)
	elif x[0] == 'NOT': # NOT
		v1 = currentSignals[x[1]]
		currentSignals[x[3]] = np.invert(v1)
	elif isNumber(x[0]) and isNumber(x[2]): # NUMBER TO NUMBER (IGNORE) 
		pass
	elif not isNumber(x[0]): # SIGNAL TO SIGNAL
		v1 = currentSignals[x[0]]
		currentSignals[x[2]] = np.uint16(v1)
	elif isNumber(x[0]): # NUMBER TO SIGNAL
		currentSignals[x[2]] = np.uint16(x[0])

def printSolution(ins):
	while len(ins) > 0:
		for i in ins:
			r = getRequiredSignals(i)
			# No requeriments for the instruction
			if len(r) == 0:
				executeInstruction(i)
				ins.remove(i)
			# There is requirements
			else:
				if checkRequirements(r):
					# Requirements are met
					executeInstruction(i)
					ins.remove(i)
	print(currentSignals['a'])

# Part 1
ins = open('input.txt').readlines()
currentSignals = {}
print("== PART 1 ==")
printSolution(ins)

# Part 2
ins = open('input-part2.txt').readlines()
currentSignals = {}
print("== PART 2 ==")
printSolution(ins)


	

