import sys

x, y = map(int, sys.stdin.readline().split())
z = (y * 100) // x
if z >= 99:
    print(-1)
else:
    res = 0
    left = 1
    right = x
 
    while left <= right:
        mid = (left + right) // 2
        if (y+mid)*100 // (x+mid) <= z:
            left = mid+1
        else:
            res = mid
            right = mid - 1
 
    print(res)