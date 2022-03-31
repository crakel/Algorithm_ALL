import sys
import math

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

b, c = map(int, sys.stdin.readline().split())

count = 0

for num in a:
    num -= b
    count += 1
    if num > 0:
        count += math.ceil(num / c)


print(count)