import sys

n, x = map(int, sys.stdin.readline().split())

visitor = list(map(int, sys.stdin.readline().split()))

left = 0
right = x-1

max_visit = -1
max_visit_cnt = 1

cu_sum = [0]
for i in range(n):
    cu_sum.append(cu_sum[-1] + visitor[i])

#print(cu_sum)

while right != n:
    #print(left, right)
    sum_visit = cu_sum[right+1] - cu_sum[left]
    #print(sum_visit)
    if sum_visit > max_visit:
        max_visit = sum_visit
        max_visit_cnt = 1

    elif sum_visit == max_visit:
        max_visit_cnt += 1

    left += 1
    right += 1

if max_visit == 0:
    print("SAD")

else:
    print(max_visit)
    print(max_visit_cnt)