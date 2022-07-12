from itertools import *

# 완탐풀이(중복조합)

def solution(n, info):
    answer = [-1]
    max_gap = -1e9
    for comb in combinations_with_replacement(range(11), n):
        lion = [0] * 11
        a_score, l_score = 0, 0

        for x in comb:
            lion[10 - x] += 1

        for i in range(11):
            if info[i] == lion[i] == 0:
                continue
            elif lion[i] > info[i]:
                l_score += 10 - i
            else:
                a_score += 10 - i

        gap = l_score - a_score
        if gap > 0 and gap > max_gap:
            max_gap = gap
            answer = lion

    return answer