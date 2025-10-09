import sys

optC = False
optP = False
for v in sys.argv:
	if v == "-c":
		optC = True
	if v == "-p":
		optP = True
	if v == "-h" or v == "--help":
		print("cat FILENAME | python3 uniq.py")
		print("  -p : print also duplicated lines to stderr")
		print("  -c : print also duplicated lines with its count to stderr")
		print("  -h : print this message")
		sys.exit()

ha = {}
for line in sys.stdin:
	if ha.get(line):
		ha[line] += 1
		if optC or optP:
			if optC:
				print(ha[line], "", end="", file=sys.stderr)
			print(line, end="", file=sys.stderr)
	else:
		print(line, end="")
		ha[line] = 1

