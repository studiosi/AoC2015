s = 0
t = "".join(open('input.txt').readlines())
x = 1
for c in t:
	if c == '(':
		s += 1
	elif c == ')':
		s -= 1
	if s == -1:
		print("X -> " + str(x))
	x += 1
print(s)
