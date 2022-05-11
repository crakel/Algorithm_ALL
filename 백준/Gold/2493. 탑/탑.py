import sys

n = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))
res = []
stack = []

for i in range(n):
    # stack = tower[:i] 시간초과?
    # list.index 쓸 시에도 시간초과
    # print(stack)
    while stack:
        if stack[-1][1] > tower[i]:
            res.append(stack[-1][0] + 1)
            break
        stack.pop()

    if not stack:
        res.append(0)
    stack.append([i, tower[i]])


for i in res:
    print(i, end=" ")