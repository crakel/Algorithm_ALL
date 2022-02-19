import sys

stack = []


def push(x):
    stack.append(x)


def pop():
    res = stack[-1]
    del stack[-1]
    return res


n = int(sys.stdin.readline())
seq = []
res = []
for _ in range(n):
    seq.append(int(sys.stdin.readline()))

seq_sorted = sorted(seq)

# print("seq : {}".format(seq))
# print("seq sort : {}".format(seq_sorted))

i = 0
j = 0
while True:
    a = -1
    if len(stack) != 0:
        a = stack[-1]

    if a == seq[i]:
        pop()
        res.append('-')
        i += 1
        if i > n - 1:
            for x in res:
                print(x)
            break

    else:
        if j > n - 1:
            print('NO')
            break

        push(seq_sorted[j])
        res.append('+')
        j += 1
        # print("sorted j번째 넣습니다 = {}".format(j))
        # print("stack = {}".format(stack))

#
# print("res : {}".format(res))
# if res.count('+') != res.count('-'):
#     print('NO')
#
# else:
#     for x in res:
#         print(x)
