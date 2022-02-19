a, b = map(int, input().split())

def GCD(a, b):
    div_a = set()
    div_b = set()

    for i in range(1, a+1):
        if a % i == 0:
            div_a.add(i)


    for i in range(1, b+1):
        if b % i == 0:
            div_b.add(i)

    res = div_a.intersection(div_b)
    return max(res)

def LCM(a, b):
    return (a *b) // GCD(a,b)

print(GCD(a,b))
print(LCM(a,b))