import sys

N, K = map(int, sys.stdin.readline().split())
lst = []
sum = 0
count = 0

for _ in range(N):
    lst.append(int(sys.stdin.readline()))

i = len(lst) - 1
while i > -1:
    quot = K // lst[i]
    if quot > 0:
        sum += quot * lst[i]
        count += quot
        K -= quot * lst[i]
    i -= 1
print(count)