import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
max_len = 0
# 최대 숫자 만큼 카운터 생성
counter = [0] * (max(a) + 1)
while left != n and right != n:
    if counter[a[right]] < k:
        counter[a[right]] += 1
        right += 1
    else:
        counter[a[left]] -= 1
        left += 1
    max_len = max(max_len, right - left)

print(max_len)
# 시간초과 (n^2)
# for i in range(len(a)):
#     cur = []
#     for j in range(i, len(a)):
#         cur.append(a[j])
#         #print(cur)
#         cur_cnt = cur.count(a[j])
#         #print(cur_cnt)
#         if cur_cnt > k:
#             break
#         max_len = max(max_len, len(cur))
#         #print("max_len : ", max_len)