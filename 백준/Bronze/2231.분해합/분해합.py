n = int(input())

res = list()

def dcmp(x):
     sum = 0
     num = x
     while x > 0:
         sum += x % 10
         x = x // 10
     return num + sum


for i in range(0, n):
    if dcmp(i) == n:
        res.append(i)

if len(res) == 0:
    print(0)

else: print(min(res))