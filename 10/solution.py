inp = "1321131112"

def divideString(s):
	r = []
	curr_c = None
	x = ""
	for c in s:
		if curr_c is None:
			curr_c = c
			x = c
		elif c == curr_c:
			x += c
		elif c != curr_c:
			r.append(x)
			curr_c = c
			x = c
	r.append(x)
	return r

def processList(l):
	s = ""
	for el in l:
		s += str(len(el))
		s += el[0]
	return s

s = inp
for x in range(40):
	l = divideString(s)
	s = processList(l)
print(len(s))

s = inp
for x in range(50):
	l = divideString(s)
	s = processList(l)
print(len(s))