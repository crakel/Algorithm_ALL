import sys

x = int(sys.stdin.readline())
dp = {1: 0}


def make_one(num):
    for i in range(2, num+1):
        if i % 3 == 0:
            if i % 2 == 0:
                dp[i] = min(dp[i//3] + 1, dp[i//2]+1, dp[i - 1] + 1)
            else:
                dp[i] = min(dp[i//3]+1, dp[i-1]+1)
        elif i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i-1]+1)
        else:
            dp[i] = dp[i-1]+1


make_one(x)
print(dp.popitem()[1])