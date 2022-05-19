import sys

n = int(sys.stdin.readline())

dic = {}

for _ in range(n):
    name, ext = sys.stdin.readline().rstrip().split('.')
    if ext not in dic:
        dic[ext] = 1
    else:
        dic[ext] += 1


for name, ext in sorted(list(dic.items())):
    print(name, ext)