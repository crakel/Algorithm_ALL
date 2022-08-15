import sys

k, n = map(int, sys.stdin.readline().split())

lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

left = 1
right = max(lan)

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for l in lan:
        cnt += l // mid

    if cnt < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)
