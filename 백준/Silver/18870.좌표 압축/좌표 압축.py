import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst_set = list(set(lst))

lst_set.sort()
dic = {}
rank = 0
for num in lst_set:
    dic[num] = rank
    rank += 1

for num in lst:
    print(dic[num], end=' ')