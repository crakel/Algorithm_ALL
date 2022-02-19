import sys

k = list(map(str, sys.stdin.readline().strip()))
stack = []
res = 0

for n in k:
    if n == ')':
        tmp = 0
        if not stack:
            print(0)
            exit(0)
        while stack:
            top = stack.pop()
            if top == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(tmp * 2)
                break

            elif top == '[':
                print(0)
                exit(0)
            else:
                tmp += top

    elif n == ']':
        tmp = 0
        if not stack:
            print(0)
            exit(0)
        while stack:
            top = stack.pop()
            if top == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(tmp * 3)
                break

            elif top == '(':
                print(0)
                exit(0)
            else:
                tmp += top
    else:
        stack.append(n)

for n in stack:
    if n == '(' or n == '[':
        print(0)
        exit(0)

    else:
        res += n

print(res)