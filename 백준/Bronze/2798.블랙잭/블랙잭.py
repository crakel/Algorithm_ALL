n, m = map(int, input().split())
card = list(map(int, input().split()))

MIN = float('inf')

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = card[i] + card[j] + card[k]
            if (sum <= m) and (m - sum <= MIN):
                MIN = m - sum
                res = sum

print(res)