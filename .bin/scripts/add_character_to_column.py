
import sys

file = open (sys.argv [1])
char = sys.argv[2]
col = int (sys.argv[3])

for line in file:
	if "ATOM" in line[:5]:
		line = line [:col] + char + line [col:]
	print line.strip()



