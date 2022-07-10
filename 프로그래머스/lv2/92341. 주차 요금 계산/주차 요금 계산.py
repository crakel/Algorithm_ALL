import math

def solution(fees, records):
    answer = []
    dic = {}
    cum = {}
    d_t, d_f, u_t, u_f = fees
    
    # 누적 주차 시간 계산
    for record in records:
        t, car, io = record.split()
        h, m = t.split(":")
        h = int(h)
        m = int(m)
        t = h * 60 + m
        
        if car not in cum:
            cum[car] = 0
        
        if io == 'IN':
            dic[car] = t
        else:
            cum[car] += t - dic[car]
            dic[car] = -1
    
    # OUT 없는 record 처리
    for car, in_t in dic.items():
        if in_t != -1:
            cum[car] += (23 * 60 + 59) - in_t
            dic[car] = -1
    
    # 누적 주차시간으로 주차 요금 계산
    for car, cum_t in dict(sorted(cum.items())).items():
        if cum_t <= d_t:
            answer.append(d_f)
        else:
            answer.append(d_f + math.ceil(((cum_t - d_t) / u_t)) * u_f)

    return answer