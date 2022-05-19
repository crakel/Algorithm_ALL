import sys

s = list(sys.stdin.readline())

res = ''
tmp = ''
flag = 0
for c in s:
    if c == '\n':
        res += tmp
    # not reverse
    if flag:
        tmp += c
        if c == '>':
            res += tmp
            tmp = ''
            flag = 0

    # reverse
    else:
        if c == '<':
            tmp += c
            flag = 1

        elif c == ' ':
            tmp += c
            res += tmp
            tmp = ''

        else:
            tmp = c + tmp

print(res)
