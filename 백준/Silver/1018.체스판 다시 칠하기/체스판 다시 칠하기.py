n, m = map(int, input().split())

board = []
counter = []

for k in range(n):
    board.append(input())

for a in range (n-7):
    for b in range (m-7):
        case_1 = 0
        case_2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        case_1 += 1
                    if board[i][j] != 'B':
                        case_2 += 1

                else:
                    if board[i][j] != 'B':
                        case_1 += 1
                    if board[i][j] != 'W':
                        case_2 += 1

        counter.append(min(case_1, case_2))

print(min(counter))