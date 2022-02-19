from collections import deque
n, m = map(int, input().split())

loc = list(map(int, input().split()))

q = deque([i for i in range(1, n+1)])
cal_count = 0

i = 0
while i < m:
    dist_left = abs(q.index(loc[i]))
    dist_right = abs(len(q) - q.index(loc[i]))

    if loc[i] == q[0]:
        q.popleft()
        i += 1

    elif dist_left > dist_right:
        q.rotate(1)
        cal_count += 1

    else:
        q.rotate(-1)
        cal_count += 1

print(cal_count)