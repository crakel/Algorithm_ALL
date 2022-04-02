import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

op = list(map(int, sys.stdin.readline().split()))

_max = -1e9
_min = 1e9


def dfs(depth, total, plus, minus, mul, div):
    global _max, _min

    if depth == n:
        _max = max(total, _max)
        _min = min(total, _min)
        return

    if plus:
        dfs(depth + 1, total + a[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - a[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth + 1, total * a[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth + 1, int(total / a[depth]), plus, minus, mul, div-1)


dfs(1, a[0], op[0], op[1], op[2], op[3])
print(_max)
print(_min)