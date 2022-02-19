import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque()

for i in range(n):
    cmd = sys.stdin.readline().strip()

    if 'push_front' in cmd:
        cmd, k = cmd.split()
        deq.appendleft(k)

    elif 'push_back' in cmd:
        cmd, k = cmd.split()
        deq.append(k)

    elif cmd == 'pop_front':
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)

    elif cmd == 'pop_back':
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)

    elif cmd == 'size':
        print(len(deq))

    elif cmd == 'empty':
        if len(deq) > 0:
            print(0)
        else:
            print(1)

    elif cmd == 'front':
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)

    elif cmd == 'back':
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)