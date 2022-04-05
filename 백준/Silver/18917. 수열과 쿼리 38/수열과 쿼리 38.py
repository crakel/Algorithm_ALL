import sys

n = int(sys.stdin.readline())

sum = 0
xor = 0

for i in range(n):
    op = list(map(int, sys.stdin.readline().split()))
    if op[0] == 1:
        sum += op[1]
        xor = xor ^ op[1]
    elif op[0] == 2 :
        sum -= op[1]
        xor = xor^op[1]
    elif op[0] == 3: print(sum)
    elif op[0] == 4: print(xor)