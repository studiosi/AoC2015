ticker = {
	
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
	
}

aunts = {}
for line in open('input.txt').readlines():
	l = line.split()
	x = {}
	for i in range(2, 8, 2):
		x[l[i].replace(':', '')] = int(l[i + 1].replace(',', ''))
	aunts[int(l[1].replace(':', ''))] = x

# Part 1	
tests = {}
for i in range(1, 501):
	j = 0
	for element in aunts[i].keys():
		if ticker[element] == aunts[i][element]:
			j += 1
	tests[i] = j
print(max(tests, key=tests.get))

# Part 2	
tests = {}
for i in range(1, 501):
	j = 0
	for element in aunts[i].keys():
		if element == 'cats' or element == 'trees':
			if ticker[element] < aunts[i][element]:
				j += 1
		elif element == 'pomeranians' or element == 'goldfish':
			if ticker[element] > aunts[i][element]:
				j += 1			
		else:
			if ticker[element] == aunts[i][element]:
				j += 1
	tests[i] = j
print(max(tests, key=tests.get))