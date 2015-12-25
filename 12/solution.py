import re
import json

inp = "".join(open('input.txt').readlines())

# Part 1 - The non-JSON way
l = re.findall(r"-?[0-9]+", inp)
x = 0
for n in l:
	x += int(n)
print(x)

# Part 2 - The JSON way
o = json.loads(inp)

def analize(o):
	n = 0
	for el in o:
		if isinstance(el, str):
			pass
		elif isinstance(el, int):
			n += el						
		elif isinstance(el, list):
			n += analize(el)
		elif isinstance(el, dict):
			if "red" not in el.values():
				n += analize(el.keys())
				n += analize(el.values())
	return n 
	
	
n = analize(o)
print(n)
