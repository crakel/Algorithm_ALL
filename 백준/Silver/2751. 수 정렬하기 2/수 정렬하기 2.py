import sys
n = int(sys.stdin.readline())
list = []

for _ in range(n):
    list.append(int(sys.stdin.readline()))

for x in sorted(list):
    print(x)