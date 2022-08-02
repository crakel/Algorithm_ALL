from itertools import *

def solution(relation):
    key = []
    row_len, col_len = len(relation[0]), len(relation)
    row = list(range(row_len))

    for i in range(1, row_len+1):
        for comb in combinations(row, i):
            tmp = []
            for r in relation:
                col = [r[c] for c in comb]
                #print(col)
                if col in tmp:
                    break
                else:
                    tmp.append(col)

            if len(tmp) == col_len:
                for k in key:
                    if set(k).issubset(set(comb)):
                        break
                else:
                    key.append(comb)

    return len(key)