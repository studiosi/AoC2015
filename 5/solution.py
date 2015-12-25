
t = open('input.txt').readlines()

# Part 1
r = 0
for s in t:
	# Condition 1
	x1 = 0 
	for c in s:
		if c in 'aeiou':
			x1 += 1
	if x1 < 3:
		continue
	# Condition 2
	x2 = False
	for i in range(len(s) - 2):
		if (s[i] == s[i+1]):
			x2 = True
			break
	if not x2:
		continue
	# Condition 3
	if 'ab' in s:
		continue
	if 'cd' in s:
		continue
	if 'pq' in s:
		continue
	if 'xy' in s:
		continue	
	r += 1
print(r)

# Part 2
r = 0
for s in t:
	# Condition 1
	strt, end = 0, 2
	x1 = False
	while end <= len(s):
		f = s[strt : end]
		rest = s[end : ]
		if f in rest:
			x1 = True
			break
		strt += 1
		end = strt + 2
	if not x1:
		continue
	# Condition 2
	x2 = False
	for i in range(len(s)-3):
		print(s)
		if s[i] == s[i+2]:
			x2 = True
			break
	if not x2:
		continue
	r += 1
print(r)

	
