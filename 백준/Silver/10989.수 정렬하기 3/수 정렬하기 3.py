import sys
n = int(sys.stdin.readline())
list = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    list[num] += 1

for i in range(len(list)):
    if list[i] != 0:
        for j in range(list[i]):
            sys.stdout.write('{}\n'.format(i))