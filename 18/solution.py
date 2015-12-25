import copy

SIZE = 100
TIMES = 100

def getVicinity(x, y):
	r = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
	r = [x for x in filter(lambda x: not (x[0] < 0 or x[1] < 0), r)]
	r = [x for x in filter(lambda x: not (x[0] > (SIZE - 1) or x[1] > (SIZE - 1)), r)]
	return r

def getCount(lights, vicinity):
	l_on = 0
	for i in vicinity:
		if lights[i[0]][i[1]] == "#":
			l_on += 1
	return l_on
	
def getLights():
	l = "".join([x.strip() for x in open("input.txt").readlines()])
	lights = [[0 for x in range(SIZE)] for x in range(SIZE)]
	(x, y) = (0, 0)
	for c in l:
		lights[x][y] = c
		x += 1
		if x == 100:
			x = 0
			y += 1
	return lights

def usesSwitch(lights, x, y, n_neighbours):
	if lights[x][y] == '#':
		if not(n_neighbours == 2 or n_neighbours == 3):
			lights[x][y] = '.'
	if lights[x][y] == '.':
		if n_neighbours == 3:
			lights[x][y] = "#"
			
def usesSwitch(lights, x, y, n_neighbours):
	if lights[x][y] == '#':
		if not(n_neighbours == 2 or n_neighbours == 3):
			lights[x][y] = '.'
	if lights[x][y] == '.':
		if n_neighbours == 3:
			lights[x][y] = "#"
			
def getTotal(lights):
	r = 0
	for x in range(SIZE):
		for y in range(SIZE):
			if lights[x][y] == "#":
				r += 1
	return r	

# Part 1	
x_current = getLights()
x_modified = copy.deepcopy(x_current)
for t in range(TIMES):
	for x in range(SIZE):
		for y in range(SIZE):
			usesSwitch(x_modified, x, y, getCount(x_current, getVicinity(x, y)))
	x_current = copy.deepcopy(x_modified)
	x_modified = copy.deepcopy(x_current)
print(getTotal(x_current))

# Part 2
x_current = getLights()
x_current[0][0] = '#'
x_current[0][99] = '#'
x_current[99][0] = '#'
x_current[99][99] = '#'
vertex = [(0,0), (0,99), (99,0), (99,99)]
x_modified = copy.deepcopy(x_current)
for t in range(TIMES):
	for x in range(SIZE):
		for y in range(SIZE):
			if (x,y) not in vertex:
				usesSwitch(x_modified, x, y, getCount(x_current, getVicinity(x, y)))
	x_current = copy.deepcopy(x_modified)
	x_modified = copy.deepcopy(x_current)
print(getTotal(x_current))


		
