import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().strip().split())

char = list(sys.stdin.readline().strip().split())
char.sort()

possible = list(combinations(char, l))

vowel = ['a', 'e', 'i', 'o', 'u']

def isPossible(string):
    vowel_cnt = 0
    conson_cnt = 0
    for char in string:
        if char in vowel:
            vowel_cnt += 1
        else:
            conson_cnt += 1
    if vowel_cnt >= 1 and conson_cnt >= 2:
        return True
    return False

res = []
for element in possible:
    if isPossible(element):
        res.append("".join(element))

res.sort()
for x in res:
    print(x)
