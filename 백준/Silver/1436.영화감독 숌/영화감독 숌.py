import sys

lst = list(map(str, range(1, 3000000)))
lst_6 = []

for k in lst:
    if '666' in k:
        lst_6.append(k)

n = int(sys.stdin.readline())
print(lst_6[n-1])