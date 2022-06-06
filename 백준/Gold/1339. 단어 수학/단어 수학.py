import sys
word = []

n = int(sys.stdin.readline())


for i in range(n):
    word.append(sys.stdin.readline().strip())

allocate = {}
for i in range(n):
    for k, x in enumerate(word[i]):
        if x not in allocate:
            allocate[x] = 10 ** (len(word[i]) - 1 - k)
        else:
            allocate[x] += 10 ** (len(word[i]) - 1 - k)


sorted_allocate = sorted(allocate, key = lambda x:allocate[x], reverse=True)
# print(allocate)
num = 9
for x in sorted_allocate:
    allocate[x] = num
    num -= 1

res = 0
# print(allocate)
for i in range(n):
    word_num = ''
    for x in word[i]:
        word_num += str(allocate[x])
    res += int(word_num)

print(res)
