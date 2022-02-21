import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

res = []


def square(paper, n):
    half = len(paper) // 2
    num = paper[0][0]

    a_list = []
    b_list = []
    c_list = []
    d_list = []

    for row in paper[:half]:
        a_list.append(row[:half])

    for row in paper[:half]:
        b_list.append(row[half:])

    for row in paper[half:]:
        c_list.append(row[:half])

    for row in paper[half:]:
        d_list.append(row[half:])

    for i in range(n):
        for j in range(n):
            if paper[i][j] != num:
                square(a_list, n//2)
                square(b_list, n//2)
                square(c_list, n//2)
                square(d_list, n//2)
                return
    if num == 1:
        res.append(1)
    else:
        res.append(0)


square(lst, n)
print(res.count(0))
print(res.count(1))
