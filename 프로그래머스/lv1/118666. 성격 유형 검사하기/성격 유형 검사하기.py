def solution(survey, choices):
    answer = ''
    
    score = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    def choose(l, r):
        if score[l] == score[r]:
            return min(l, r)
        else:
            if score[l] > score[r]:
                return l
            else:
                return r
    
    for s, c in zip(survey, choices):
        l, r = s[0], s[1]
        if c == 1:
            score[l] += 3
        elif c == 2:
            score[l] += 2
        elif c == 3:
            score[l] += 1
        elif c == 4:
            continue
        elif c == 5:
            score[r] += 1
        elif c == 6:
            score[r] += 2
        elif c == 7:
            score[r] += 3
    
    answer += choose('R', 'T')
    answer += choose('C', 'F')
    answer += choose('J', 'M')
    answer += choose('A', 'N')
    
    return answer
        