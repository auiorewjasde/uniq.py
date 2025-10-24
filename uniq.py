import sys
import argparse
from collections import defaultdict

def main():
	parser = argparse.ArgumentParser(
		description="A uniq-like program that works without sorting the input."
	)
	parser.add_argument(
		"-p",
		action="store_true",
		help="Print duplicated lines to stderr."
	)
	parser.add_argument(
		"-c",
		action="store_true",
		help="Print duplicated lines with their count to stderr."
	)

	args = parser.parse_args()

	counts = defaultdict(int)

	if sys.stdin.isatty():
		parser.print_help()
		sys.exit(0)

	for line in sys.stdin:
		counts[line] += 1
		if counts[line] == 1:
			# first occurrence → stdout
			print(line, end="")
		else:
			# duplicate
			if args.c:
				print(counts[line], "", end="", file=sys.stderr)
			if args.p or args.c:
				print(line, end="", file=sys.stderr)

if __name__ == "__main__":
	main()
