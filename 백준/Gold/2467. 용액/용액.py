import sys

n = int(sys.stdin.readline())

sol = list(map(int, sys.stdin.readline().split()))

if len(sol) == 2:
    print(sol[0], sol[1])
    exit(0)

close_lst = []
close = sys.maxsize
sol_left = 0
sol_right = 0

for i in range(n-1):
    left = i + 1
    right = n - 1
    cur = sol[i]

    while left <= right:
        mid = (left + right) // 2
        mix = cur + sol[mid]
        if abs(mix) < close:
            close = abs(mix)
            sol_left = i
            sol_right = mid
            if mix == 0:
                break

        if mix < 0:
            left = mid + 1

        else:
            right = mid - 1

print(sol[sol_left], sol[sol_right])
