import sys

n = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
del_n = int(sys.stdin.readline())

tree = {}
leaf = 0

for i in range(n):
    tree[i] = parent[i]

tree[del_n] = -2


def del_node(node):
    for i, v in tree.items():
        if v == node:
            del_node(i)
            tree[i] = -2


del_node(del_n)

for k in range(n):
    is_leaf = True
    if tree[k] == -2:
        continue

    for i, v in tree.items():
        if v == k:
            is_leaf = False
            break
    if is_leaf:
        leaf += 1

print(leaf)