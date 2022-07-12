from itertools import *
from collections import *

def solution(orders, course):
    answer = []

    for n in course:
        able = []
        for order in orders:
            order = sorted(order)
            able.extend(list(combinations(order, n)))

        cnt = Counter(able)
        
        if cnt:
            max_cnt = max(cnt.values())

        if max_cnt >= 2:
            for key,value in cnt.items():
                if value == max_cnt:
                    answer.append(''.join(key))

    return sorted(answer)