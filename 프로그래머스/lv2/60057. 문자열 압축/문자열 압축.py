def solution(s):
    answer = 1e9
    
    for i in range(1, len(s)//2+2):
        cur = s[:i]
        cnt = 1
        res = ""
        
        for j in range(i, len(s)+i, i):

            if cur == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += cur
                else:
                    res += str(cnt) + cur
                cnt = 1
                cur = s[j:j+i]
        
        answer = min(answer, len(res))
        
    return answer