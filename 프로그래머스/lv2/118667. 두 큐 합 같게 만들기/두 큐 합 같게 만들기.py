from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    cnt = 0
    flag = 0
    sum1, sum2 = sum(q1), sum(q2)
    while q1 and q2 and cnt != len(queue1) * 3:
        if sum1 == sum2:
            return cnt
        
        if sum1 > sum2:
            tmp = q1.popleft()
            sum1 -= tmp
            sum2 += tmp
            q2.append(tmp)
            cnt += 1
        else:
            tmp = q2.popleft()
            sum2 -= tmp
            sum1 += tmp
            q1.append(tmp)
            cnt += 1
    
    return -1