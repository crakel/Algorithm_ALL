import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    cmd = sys.stdin.readline().strip().split()

    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    x = int(cmd[1])

    if cmd[0] == 'add':
        s.add(x)

    elif cmd[0] == 'remove':
        s.discard(x)

    elif cmd[0] == 'check':
        print(1 if x in s else 0)

    elif cmd[0] == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)