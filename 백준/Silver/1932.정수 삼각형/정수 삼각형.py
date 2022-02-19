import sys

n = int(sys.stdin.readline())

t = []
res = []
for i in range(n, 0, -1):
    if i == n:
        t.append(list(map(int, '0' * ((2*n) + 1))))
    num = list(sys.stdin.readline().strip().split())
    tmp = []
    for j in range(len(num)):
        tmp.append(num[j])
        if j < len(num) - 1:
            tmp.append('0')
            
    t.append(list(map(int, i * ['0'] + tmp + i * ['0'])))

for i in range(1, n+1):
    for j in range(1, n*2):
        t[i][j] = t[i][j] + max(t[i-1][j-1], t[i-1][j+1])

print(max(t[-1]))
