inp = 'cqjxjnds'

def increment(s):
	x = s[-1]
	if x == 'z':
		s = s[:-1] + 'a'
		i = -1
		while True:
			i -= 1
			if i == -(len(s) + 1):
				 s = 'a' + s
				 break
			elif s[i] != 'z':
				s = s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]
				break
			else:
				s = s[:i] + 'a' + s[i + 1:]
	else:
		s = s[:-1] + chr(ord(s[-1]) + 1)
	return s

def validate_1(s):
	for i in range(len(s) - 2):
		if ord(s[i]) == ord(s[i + 1]) - 1 and ord(s[i + 1]) == ord(s[i + 2]) - 1:
			return True
	return False

def validate_2(s):
	if 'i' in s:
		return False
	if 'o' in s:
		return False
	if 'l' in s:
		return False
	return True
	
def validate_3(s):
	pair_letters = []
	i = 0
	while i < len(s) - 1:
		if s[i] == s[i + 1]:
			if s[i] not in pair_letters:
				pair_letters.append(s[i])
			i += 1
		i += 1
	return len(pair_letters) >= 2
	
def validate(s):
	return validate_2(s) and validate_3(s) and validate_1(s) 
	
s = inp
x = ""
while True: 
	while not validate(s):
		s =	increment(s)
	print(s)
	x = input()
	if 'x' in x:
		break
	else:
		s = increment(s)

#print(validate_1('cqjxkkkj'))
#print(validate_2('cqjxkkkj'))
#print(validate_3('cqjxkkkj'))