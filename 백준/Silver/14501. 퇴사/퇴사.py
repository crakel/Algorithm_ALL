import sys

n = int(sys.stdin.readline())

dp = {i: 0 for i in range(1, n+2)}
table = {}

for i in range(1, n+1):
    table[i] = tuple(map(int, sys.stdin.readline().split()))

# 뒤 인덱스부터 누적 접근
for i in range(n, 0, -1):
    if table[i][0] + i > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(table[i][1] + dp[i + table[i][0]], dp[i+1])

# 틀린 접근
# for i in range(1, n+1):
#     j = i
#     prev = 0
#     while j <= n:
#         if j + table[j][0] <= n+1:
#             dp[j] = max(dp[prev] + table[j][1], dp[j])
#             prev = j
#         j += table[j][0]

print(dp[1])