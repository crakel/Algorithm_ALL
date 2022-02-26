import sys

def fibonacci(n):
    dp[0] = 0

    if n > 0:
        dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dp = {}
    fibonacci(n)
    one = dp.popitem()[1] if n > 0 else 0
    zero = dp.popitem()[1] if n > 0 else 1
    print(zero, one)