import sys
import math

n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1] = 1

if n == int(math.sqrt(n))**2:
    print(1)
    exit(0)


for i in range(2, n+1):
    if i == int(math.sqrt(i))**2:
        dp[i] = 1
    else:
        min_v = 50001
        for j in range(1, math.floor(math.sqrt(i))+1):
            min_v = min(min_v, dp[i - j**2] + 1)
        dp[i] = min_v

print(dp[n])