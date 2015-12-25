ls = open('input.txt').readlines()

# part 1
t = 0
for l in ls:
	(l, w, h) = l.split('x')
	(ln, wn, hn) = (int(l), int(w), int(h))
	(d1, d2, d3) = (ln*wn, wn*hn, hn*ln)
	t += min(d1, d2, d3)
	t += (2*d1 + 2*d2 + 2*d3)
print(t)

# part 2
t = 0
for l in ls:
	(l, w, h) = l.split('x')
	(ln, wn, hn) = (int(l), int(w), int(h))
	p1 = 2*wn + 2*hn
	p2 = 2*ln + 2*hn
	p3 = 2*wn + 2*ln
	t += min(p1, p2, p3)
	t += ln * wn * hn
print(t)