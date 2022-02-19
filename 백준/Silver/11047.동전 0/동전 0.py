import sys

N, K = map(int, sys.stdin.readline().split())
lst = []
sum = 0
count = 0

for _ in range(N):
    lst.append(int(sys.stdin.readline()))

i = len(lst) - 1
while i > -1:
    if sum + lst[i] <= K:
        sum += lst[i]
        count += 1
        i += 1
    i -= 1

print(count)