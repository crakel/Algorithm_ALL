import sys

n = int(sys.stdin.readline())


def fac(num):
    res = 1
    for n in range(num, 1, -1):
        res *= n
    return res


res = str(fac(n))
count = 0

for i in range(1, len(res)+1):
    if res[-i] == '0':
        count += 1
    else:
        print(count)
        exit(0)