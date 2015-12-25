
inp = open('input.txt').readlines()

SIZE = 1000

def turn_on(lights, x1, y1, x2, y2):
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			lights[x][y] = 1

def turn_off(lights, x1, y1, x2, y2):
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			lights[x][y] = 0

def toggle(lights, x1, y1, x2, y2):
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			if lights[x][y] == 1:
				lights[x][y] = 0
			elif lights[x][y] == 0:
				lights[x][y] = 1

def count(lights):
	i = 0
	for x in range(SIZE):
		for y in range(SIZE):
			i += lights[x][y]
	return i

def turn_on_2(lights, x1, y1, x2, y2):
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			lights[x][y] += 1

def turn_off_2(lights, x1, y1, x2, y2):
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			lights[x][y] -= 1
			if lights[x][y] < 0:
				lights[x][y] = 0

def toggle_2(lights, x1, y1, x2, y2):
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			lights[x][y] += 2


# Part 1
lights = [[0 for x in range(SIZE)] for y in range(SIZE)]
for instr in inp:
	x = instr.split()
	if instr.startswith('turn on'):
		p1, p2 = x[2].split(','), x[4].split(',')
		turn_on(lights, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
	elif instr.startswith('turn off'):
		p1, p2 = x[2].split(','), x[4].split(',')
		turn_off(lights, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
	elif instr.startswith('toggle'):
		p1, p2 = x[1].split(','), x[3].split(',')
		toggle(lights, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
print(count(lights))

# Part 2
lights = [[0 for x in range(SIZE)] for y in range(SIZE)]
for instr in inp:
	x = instr.split()
	if instr.startswith('turn on'):
		p1, p2 = x[2].split(','), x[4].split(',')
		turn_on_2(lights, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
	elif instr.startswith('turn off'):
		p1, p2 = x[2].split(','), x[4].split(',')
		turn_off_2(lights, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
	elif instr.startswith('toggle'):
		p1, p2 = x[1].split(','), x[3].split(',')
		toggle_2(lights, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))
print(count(lights))