n = list(input())

num = ['2', '3', '4', '5', '6', '7', '8', '9']
res = [0] * 100
mass = {'H':1, 'C':12, 'O':16}

i = 0 # 괄호의 깊이
for x in n:
    if x in mass:
        tmp = mass[x]
        res[i] += tmp

    elif x == '(':
        i+= 1
        res[i] = 0

    elif x == ')':
        tmp = res[i]
        i-= 1
        res[i] += tmp


    elif x in num:
        res[i] += tmp * (int(x) - 1)

print(res[0])