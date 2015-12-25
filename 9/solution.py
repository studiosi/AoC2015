import itertools

vertex_input = open('input.txt').readlines()

def getDistance(graph, origin, destination):
	if not destination in graph[origin].keys():
		return None
	return graph[origin][destination]

def pairs(cities):
	a, b = itertools.tee(cities)
	next(b, None)
	return zip(a, b)

def process_vertex(v):
	x1 = v.split('to')
	origin = x1[0].strip().upper()
	x2 = x1[1].split('=')
	destiny = x2[0].strip().upper()
	cost = int(x2[1].strip())
	return (origin, destiny, cost)

vertex_list = []
for v in vertex_input:
	vertex_list.append(process_vertex(v))

graph = {}
for v in vertex_list:
	if v[0] not in graph.keys():
		graph[v[0]] = {}
	if v[1] not in graph.keys():
		graph[v[1]] = {}

for v in vertex_list:
	graph[v[0]][v[1]] = v[2]
	graph[v[1]][v[0]] = v[2]

# Let's suppose there is no isolated city
cities = graph.keys()

min_dist = None
max_dist = None

for order in itertools.permutations(cities):
	set_dist = True
	current_total = 0
	for origin, destination in pairs(order):
		d = getDistance(graph, origin.upper(), destination.upper())
		if d is None:
			set_dist = False
			break
		current_total += d
	if set_dist:
		if min_dist is None or current_total < min_dist:
			min_dist = current_total
		if max_dist is None or current_total > max_dist:
			max_dist = current_total

print("MIN: " + str(min_dist))
print("MAX: " + str(max_dist))

