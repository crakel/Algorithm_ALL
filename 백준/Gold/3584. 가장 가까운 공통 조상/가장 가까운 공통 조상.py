import sys
sys.setrecursionlimit(10**9)
t = int(sys.stdin.readline())

# 각 노드별 루트노드까지 depth를 계산해 추후 비교
def dfs(cur, depth):
    visited[cur] = 1
    d[cur] = depth
    for n in tree[cur]:
        if not visited[n]:
            dfs(n, depth+1)

for _ in range(t):
    n = int(sys.stdin.readline())
    tree = {i: [] for i in range(n + 1)}
    # 노드 1번부터 시작
    parent = [0] * (n + 1)
    d = [0] * (n + 1)
    visited = [0] * (n + 1)

    for __ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        parent[b] = a
    # root node 검색
    for i in range(1, n + 1):
        if parent[i] == 0:
            dfs(i, 0)
            break

    p, q = map(int, sys.stdin.readline().split())

    # 조상 비교할 depth 까지 올라옴
    while d[p] != d[q]:
        if d[p] > d[q]:
            p = parent[p]
        else:
            q = parent[q]

    while p != q:
        p = parent[p]
        q = parent[q]

    print(p)
