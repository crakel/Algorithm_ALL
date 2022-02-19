a = list(input())

if len(a) < 2:
    a.insert(0, '0')

i = 0
c = a

start = "".join(a)

while True:
    temp = list(str(int(c[0]) + int(c[1])))
    if (int(c[0]) + int(c[1]) >= 10):
        b = temp[1]

    else:
        b = temp[0]

    c = c[1] + b

    if c != start:
        i += 1

    elif c == start:
        i += 1
        break

print(i)