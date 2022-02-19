board = []
blank = []

for _ in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])


def isPromise(i, j):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if board[i][k] in num:
            num.remove(board[i][k])
        if board[k][j] in num:
            num.remove(board[k][j])

    i //= 3
    j //= 3

    for a in range(i*3, (i+1)*3):
        for b in range(j*3, (j+1)*3):
            if board[a][b] in num:
                num.remove(board[a][b])

    return num


done = False
def dfs(x):
    global done

    if done:
        return

    if x == len(blank):
        for row in board:
            print(*row)
        done = True
        return

    else:
        i = blank[x][0]
        j = blank[x][1]
        promise = isPromise(i, j)

        for num in promise:
            board[i][j] = num
            dfs(x+1)
            board[i][j] = 0

dfs(0)