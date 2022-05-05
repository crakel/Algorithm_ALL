import sys

n = int(sys.stdin.readline())

budget = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

left = 0
right = max(budget)

max_budget = left
while left <= right:
    sum_budget = 0
    mid = (left + right) // 2

    for b in budget:
        if mid > b:
            sum_budget += b
        else:
            sum_budget += mid

    if sum_budget <= total:
        left = mid + 1
        max_budget = mid
    else:
        right = mid - 1

print(max_budget)
