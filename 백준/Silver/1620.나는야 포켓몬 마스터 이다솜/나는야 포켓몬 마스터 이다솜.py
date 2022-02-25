import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}

for i in range(1, n+1):
    s = sys.stdin.readline().rstrip()
    dic[i] = s
    dic[s] = i

for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])