import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    dic[s] = 1

res = 0
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    if s in dic:
        res += 1

print(res)
