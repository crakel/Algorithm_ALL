import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

circle = deque(range(1, n + 1))
index = k
per = []

for i in range(len(circle)):
    circle.rotate(-k + 1)
    per.append(circle.popleft())
    
print("<{}>".format(", ".join(map(str, per))))