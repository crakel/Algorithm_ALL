import sys

n = int(sys.stdin.readline())

sol = list(map(int, sys.stdin.readline().split()))

sol.sort()
#print(sol)

if len(sol) == 3:
    print(sol[0], sol[1], sol[2])
    exit(0)


closest = sys.maxsize
for fix in range(n-2):
    left = fix + 1
    right = n - 1
    while left < right:
        mix = sol[fix] + sol[left] + sol[right]
        if abs(mix) < closest:
            ans = (sol[fix], sol[left], sol[right])
            closest = abs(mix)
            if closest == 0:
                break

        if mix < 0:
            left += 1
        else:
            right -= 1

print(*ans)


# left 와 right 고정하고 mid안에서 도는 풀이 : 틀림, 반례 못찾음
# left = 0
# right = n - 1
# mid = 1
# sol_left, sol_mid, sol_right = left, mid, right
# close = sol[left] + sol[mid] + sol[right]
# mix = close
# while left + 1 < right:
#     m = left + 1
#
#     for m in range(left+1, right):
#         mix = sol[left] + sol[m] + sol[right]
#         #print(left,m,right, mix)
#         if abs(mix) < abs(close):
#             sol_left = left
#             sol_right = right
#             sol_mid = m
#             close = mix
#
#             if close == 0:
#                 break
#     #print(close)
#
#     if abs(close) >= abs(mix):
#         left += 1
#
#     else:
#         right -= 1
#
# print(sol[sol_left], sol[sol_mid], sol[sol_right])
