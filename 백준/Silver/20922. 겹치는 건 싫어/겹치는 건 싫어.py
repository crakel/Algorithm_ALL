import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
max_len = 0
# 최대 숫자 만큼 카운터 생성 -> 딕셔너리로 성능 향상 x
# 실제 크기만큼 배열 생성하는게 오히려 더 빠르다.
counter = [0] * (max(a) + 1)
# counter = {i: 0 for i in a}
# counter = {}
while left != n and right != n:
    # if a[right] not in counter:
    #     counter[a[right]] = 0
    #
    # if a[left] not in counter:
    #     counter[a[left]] = 0

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
