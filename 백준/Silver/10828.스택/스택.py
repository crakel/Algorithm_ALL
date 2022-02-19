import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    cmd = sys.stdin.readline().strip()
    if 'push' in cmd:
        cmd, k = cmd.split()
        deq.append(k)
    elif cmd == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif cmd == 'size':
        print(len(deq))
    elif cmd == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])