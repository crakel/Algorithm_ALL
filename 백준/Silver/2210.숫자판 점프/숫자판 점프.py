import sys

table = []
for _ in range(5):
    table.append(list(sys.stdin.readline().strip().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num_list = []
def dfs(x, y, num):
    if len(num) == 6:
        if num not in num_list:
            num_list.append(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + table[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, table[i][j])
print(len(num_list))