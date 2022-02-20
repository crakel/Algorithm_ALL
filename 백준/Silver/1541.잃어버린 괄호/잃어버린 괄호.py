import sys

exps = list(sys.stdin.readline().strip().split('-'))
temps = []
res = []

for exp in exps:
    temps.append(exp.split('+'))

for temp in temps:
    temp_sum = 0
    for t in temp:
        temp_sum += int(t)
    res.append(temp_sum)

print(res[0] - sum(res[1:]))