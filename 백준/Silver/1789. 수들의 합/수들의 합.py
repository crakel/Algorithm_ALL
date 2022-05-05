import sys

s = int(sys.stdin.readline())

# n_sum = [1]
#
# i = 1
# while True:
#     #print(n_sum[i-1] + i + 1)
#     if n_sum[i-1] + i + 1 > s:
#         break
#
#     n_sum.append(n_sum[i-1] + i + 1)
#     i += 1
#
# #print(n_sum)
# print(len(n_sum))

# 이분탐색 풀이
ans = 0
left = 1
right = s

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)