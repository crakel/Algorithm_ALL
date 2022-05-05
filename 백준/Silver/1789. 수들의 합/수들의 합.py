import sys

s = int(sys.stdin.readline())

n_sum = [1]

i = 1
while True:
    #print(n_sum[i-1] + i + 1)
    if n_sum[i-1] + i + 1 > s:
        break

    n_sum.append(n_sum[i-1] + i + 1)
    i += 1

#print(n_sum)
print(len(n_sum))