import sys

n = int(sys.stdin.readline())

socks = list(sys.stdin.readline().split())
a = []

i = 0
while socks:
    if a and socks[-1] == a[-1]:
        socks.pop()
        a.pop()
        i += 1
    else:
        a.append(socks[-1])
        socks.pop()

if not a:
    print(i*2)
else:
    print("impossible")