import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))


res = []


def square(paper, n):
    div = n // 3
    num = paper[0][0]

    a_list = []
    b_list = []
    c_list = []
    d_list = []
    e_list = []
    f_list = []
    g_list = []
    h_list = []
    i_list = []

    for row in paper[:div]:
        a_list.append(row[:div])

    for row in paper[:div]:
        b_list.append(row[div:2*div])

    for row in paper[:div]:
        c_list.append(row[2*div:3*div])

    for row in paper[div:2*div]:
        d_list.append(row[:div])

    for row in paper[div:2*div]:
        e_list.append(row[div:2*div])

    for row in paper[div:2*div]:
        f_list.append(row[2*div:3*div])

    for row in paper[2*div:3*div]:
        g_list.append(row[:div])

    for row in paper[2*div:3*div]:
        h_list.append(row[div:2*div])

    for row in paper[2*div:3*div]:
        i_list.append(row[2*div:3*div])

    temp = []
    for p in paper:
        temp.extend(p)

    if temp.count(num) != n*n:
        square(a_list, div)
        square(b_list, div)
        square(c_list, div)
        square(d_list, div)
        square(e_list, div)
        square(f_list, div)
        square(g_list, div)
        square(h_list, div)
        square(i_list, div)
        return

    # for i in range(n):
    #     for j in range(n):
    #         if paper[i][j] != num:
    #             square(a_list, div)
    #             square(b_list, div)
    #             square(c_list, div)
    #             square(d_list, div)
    #             square(e_list, div)
    #             square(f_list, div)
    #             square(g_list, div)
    #             square(h_list, div)
    #             square(i_list, div)
    #             return
    if num == 1:
        res.append(1)
    elif num == -1:
        res.append(-1)
    else:
        res.append(0)


square(lst, n)
print(res.count(-1))
print(res.count(0))
print(res.count(1))