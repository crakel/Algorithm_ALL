import sys

n, k = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline())

cnt = k

s = []
for i in range(n):
    while k > 0 and s and s[-1] < num[i]:
        s.pop()
        k -= 1
    s.append(num[i])

print(''.join(s[:n-cnt]))