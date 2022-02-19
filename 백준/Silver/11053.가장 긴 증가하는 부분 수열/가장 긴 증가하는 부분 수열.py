n = int(input())

res = [1] * n
a = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            res[i] = max(res[i], res[j] + 1)

print(max(res))
