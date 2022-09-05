# 상 하 좌 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(board, aloc, bloc):
    # A는 최소 B는 최대일떄 합의 최소

    return move_a(aloc, bloc, board, 0)[1]


# return (승리여부, 이동횟수)
def move_a(aloc, bloc, board, move_cnt):
    if not board[aloc[0]][aloc[1]]:
        return (False, move_cnt)

    win = []
    lose = []

    flag = False

    for d in dir:
        nr, nc = aloc[0] + d[0], aloc[1] + d[1]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]:
            flag = True
            nb = [r[:] for r in board]
            nb[aloc[0]][aloc[1]] = 0

            nxt = move_b([nr, nc], bloc, nb, move_cnt + 1)

            if not nxt[0]:
                win.append(nxt[1])
            else:
                lose.append(nxt[1])

    if flag:
        if win:
            return (True, min(win))
        else:
            return (False, max(lose))

    return (False, move_cnt)


def move_b(aloc, bloc, board, move_cnt):
    if not board[bloc[0]][bloc[1]]:
        return (False, move_cnt)
    win = []
    lose = []

    flag = False
    for d in dir:
        nr, nc = bloc[0] + d[0], bloc[1] + d[1]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]:
            flag = True
            nb = [r[:] for r in board]
            nb[bloc[0]][bloc[1]] = 0

            nxt = move_a(aloc, [nr, nc], nb, move_cnt + 1)

            if not nxt[0]:
                win.append(nxt[1])
            else:
                lose.append(nxt[1])

    if flag:
        if win:
            return (True, min(win))
        else:
            return (False, max(lose))

    return (False, move_cnt)

