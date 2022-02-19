import sys

n = int(sys.stdin.readline())

op = ['+', '-', '*', '/']
num = []
stack = []
exps = list(map(str, sys.stdin.readline().strip()))

for i in range(n):
    k = int(sys.stdin.readline())
    num.append(k)

for i in range(len(exps)):
    if exps[i] not in op:
        exps[i] = num[ord(exps[i]) - ord('A')]

for exp in exps:
    if exp in op:
        b = stack.pop()
        a = stack.pop()
        if exp == '+':
            stack.append(a + b)

        elif exp == '-':
            stack.append(a - b)

        elif exp == '*':
            stack.append(a * b)

        elif exp == '/':
            stack.append(a / b)

    else:
        stack.append(exp)

print("{:.2f}".format(stack[0]))