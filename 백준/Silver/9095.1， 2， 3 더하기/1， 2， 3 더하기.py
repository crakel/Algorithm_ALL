import sys

t = int(sys.stdin.readline())
dp = {1: 1, 2: 2, 3: 4}


def sum_case(num):
    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for _ in range(t):
    n = int(sys.stdin.readline())
    sum_case(n)
    print(dp[n])
