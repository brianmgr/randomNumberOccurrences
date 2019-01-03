import sys
import time
import random

seed = 0
counter = 1
integers = {"0":0,
	"1":0,
	"2":0,
	"3":0,
	"4":0,
	"5":0,
	"6":0,
	"7":0,
	"8":0,
	"9":0}

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

print("\nCreating random 32 bit integers. Press Ctrl+C to finish.\n")
time.sleep(2)
print("    Run      Integer")

try:
	while seed != 1:
		seed = random.getrandbits(32)
		print("    %s    %s") %(counter,seed)
		delete_last_lines(n=1)
		counter += 1
		seedBits = [int(i) for i in str(seed)]
		for bit in seedBits:
			for integer in integers:
				if str(bit) == integer[0]:
					integers[integer] += 1
except KeyboardInterrupt:
	time.sleep(0.3)
	delete_last_lines(n=4)
	print("\nOccurrences of individual numbers in random 32 bit integers:")
	print("\n    Num   Count")
	print ("    ---|---------")
	for integer in sorted(integers.iterkeys()):
		print ("     %s    %s") %(integer, integers[integer])
		print ("    ---|---------")
		
