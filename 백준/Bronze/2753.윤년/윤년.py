import sys

n = int(sys.stdin.readline())

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print(1)
else:
    print(0)