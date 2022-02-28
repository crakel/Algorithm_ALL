import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

count = 0
ioi_count = 0
i = 1

while i < m - 1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        ioi_count += 1
        if ioi_count == n:
            count += 1
            ioi_count -= 1
        i += 1
    else:
        ioi_count = 0
    i += 1

print(count)