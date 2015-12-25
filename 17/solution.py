import itertools

containers = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]

# Part 1 & 2 (partially)
r = 0
s = {}
for i in range(1, len(containers) + 1):
	for c in itertools.combinations(containers, i):
		if sum(c) == 150:
			r += 1
			if len(c) not in s.keys():
				s[len(c)] = [c]
			else:
				s[len(c)].append(c)
print(r)

# Part 2 (the rest)
m = min(s.keys())
print(len(s[m]))