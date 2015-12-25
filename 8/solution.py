import ast

inp = open('input.txt').readlines()

print("== PART 1 ==")
code_length = 0
real_length = 0
for s in inp:
	s = s.strip()
	code_length += len(s)
	real_length += len(ast.literal_eval(s))

print('code: ' + str(code_length))
print('real: ' + str(real_length))
print('solution: ' + str(code_length - real_length))

print("== PART 2 ==")
code_length = 0
real_length = 0
for s in inp:
	s = s.strip()
	real_length += len(s)
	code_length += len(str(s.encode())) + s.count('"') - 1

print('code: ' + str(code_length))
print('real: ' + str(real_length))
print('solution: ' + str(code_length - real_length))