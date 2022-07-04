t = int(input())
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우


def dfs(r, c, is_cut, route):
    global max_route

    if route > max_route:
        max_route = route

    visited[r][c] = 1

    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if not 0 <= nr < n or not 0 <= nc < n:
            continue

        if not visited[nr][nc]:
            if field[r][c] > field[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, is_cut, route+1)
                visited[nr][nc] = 0

            else:
                if not is_cut:
                    for cut in range(1, k+1):
                        field[nr][nc] -= cut
                        is_cut = 1
                        if field[r][c] > field[nr][nc]:
                            visited[nr][nc] = 1
                            dfs(nr, nc, is_cut, route+1)
                            visited[nr][nc] = 0
                        is_cut = 0
                        field[nr][nc] += cut


def max_h_idx(h):
    res = []
    for r in range(n):
        for c in range(n):
            if field[r][c] == h:
                res.append((r, c))
    return res


for i in range(1, t + 1):
    n, k = map(int, input().split())
    field = []
    max_route = 0
    for _ in range(n):
        field.append(list(map(int, input().split())))

    max_h = max(map(max, field))
    for r, c in max_h_idx(max_h):
        visited = [[0] * n for _ in range(n)]
        dfs(r, c, 0, 1)
    print("#{} {}".format(i, max_route))
    