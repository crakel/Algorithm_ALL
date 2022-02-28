import sys

n, m = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

sum_temp = [0]
temp = 0
for num in lst:
    temp += num
    sum_temp.append(temp)


for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_temp[j] - sum_temp[i-1])