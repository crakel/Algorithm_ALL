import sys

dic = {}
total = 0

while True:
    n = sys.stdin.readline().strip()
    if not n:
        break

    if n not in dic:
        dic[n] = 1

    else:
        dic[n] += 1

for i in dic:
    total += dic[i]

for i in dic:
    dic[i] = dic[i] / total * 100

sorted_list = sorted(dic.items())

for n in sorted_list:
    print(f'{n[0]} {n[1]:.4f}')