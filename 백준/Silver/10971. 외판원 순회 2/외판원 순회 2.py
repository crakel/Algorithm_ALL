import sys
# TSP : Traveling Salesman problem
n = int(sys.stdin.readline())
w = []
res = []

for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))

min_cst = sys.maxsize


def bt(start, next, cst, visited):
    global min_cst
    if len(visited) == n:
        if w[next][start]:
            min_cst = min(min_cst, cst + w[next][start])
        return

    for i in range(n):
        if w[next][i] and i not in visited and cst < min_cst:
            visited.append(i)
            bt(start, i, cst + w[next][i], visited)
            visited.pop()


for i in range(n):
    bt(i, i , 0, [i])

print(min_cst)