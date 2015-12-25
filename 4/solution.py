import hashlib

t = 'iwrupvqb'
i = 1

N_ZEROS = 6

# Part 1 & 2 (Change N_ZEROS)
while True:
	m = hashlib.md5()
	x = (t + str(i)).encode('ascii', 'ignore')
	m.update(x)
	s = m.hexdigest()
	if(i % 100000 == 0):
		print('X -> ' + str(x))
	if(s[0:N_ZEROS] == '0' * N_ZEROS):
		print('OK -> ' + str(x))
		break
	i += 1