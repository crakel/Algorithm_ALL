import sys

N = int(sys.stdin.readline())
lst = []
times = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    lst.append((s, e))

lst.sort(key = lambda x: (x[1], x[0]))

for t in lst:
    if not times:
        times.append((t[0], t[1]))
        continue

    if t[0] >= times[-1][1]:
        times.append((t[0], t[1]))

print(len(times))

# 시간초과 코드

# lst.sort()
# for p in lst:
#     times = []
#     times.append((p[0], p[1], p[2]))
#     for k in lst:
#         flag = True
#         #print(times)
#         for time in times:
#             #print(time)
#             if time[1] < k[2] and time[2] > k[1]:
#                 flag = False
#
#         if flag:
#             times.append((k[0], k[1], k[2]))
#     case.append(len(times))
#
# print(max(case))