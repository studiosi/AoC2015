t = "".join(open('input.txt').readlines())

# First Part
v = set()
(x, y) = (0, 0)
v.add((0,0))
for c in t:
	if c == '^':
		y += 1
	elif c == 'v':
		y -= 1
	elif c == '>':
		x += 1
	elif c == '<':
		x -= 1
	v.add((x, y))
print(len(v))

# Second Part
v = set()
v.add( (0,0) )
(xS, yS) = (0, 0)
(xR, yR) = (0, 0)
turn = "SANTA"
for c in t:
	if c == '^':
		if turn == "SANTA":
			yS += 1
		if turn == "ROBOT":
			yR += 1
	elif c == 'v':
		if turn == "SANTA":
			yS -= 1
		if turn == "ROBOT":
			yR -= 1
	elif c == '>':
		if turn == "SANTA":
			xS += 1
		if turn == "ROBOT":
			xR += 1
	elif c == '<':
		if turn == "SANTA":
			xS -= 1
		if turn == "ROBOT":
			xR -= 1
	if turn == "SANTA":
		turn = "ROBOT"
		v.add((xS, yS))		
	elif turn == "ROBOT":
		turn = "SANTA"
		v.add((xR, yR))
print(len(v))

		
