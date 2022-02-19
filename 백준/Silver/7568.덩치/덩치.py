n = int(input())
a = []
res = []

for i in range(n):
    a.append([])
    a[i] = list(map(int, input().split()))

for j in range(n):
    rank = 1
    for k in range(n):
        if a[j][0] < a[k][0] and a[j][1] < a[k][1]:
                rank += 1

    res.append(rank)

for x in res:
    print(x, end=' ')
