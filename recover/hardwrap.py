import sys

def hwrap(line):
	if len(line) <= 80 or line.startswith('    '):
		return line

	cut = line.rfind(' ', 0, 81)

	if cut == -1:
		return line # Fuck it
	else:
		return line[:cut] + '\n' + hwrap(line[cut + 1:])

filename = sys.argv[-1]

with open(filename) as f:
	source = f.read().split('\n')

with open(filename, 'w') as f:
	for line in source:
		f.write(hwrap(line) + '\n')