import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    res = deque()
    ps = deque(map(str, sys.stdin.readline().strip()))
    for j in ps:
        if j == ')':
            if len(res) == 0:
                res.append(j)
                break
            res.popleft()
        else:
            res.append(j)

    if len(res) == 0:
        print('YES')

    else:
        print('NO')