def is_b(s):
    if s.count('(') == s.count(')'):
        return True
    return False

def is_c(s):
    if not is_b(s):
        return False
    else:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
    
def sep_b(s):
    l, r = 0, 0
    for i, c in enumerate(s):
        if c == '(':
            l += 1
        else:
            r += 1
        
        if l > 0 and r > 0 and l == r:
            break
    
    u, v = s[:i+1], s[i+1:]
    return u, v
        
def solution(p):
    answer = ''
    
    #1
    if not len(p):
        return ''
    #2
    u, v = sep_b(p)
    #3
    if is_c(u):
        return u + solution(v)
    
    #4
    answer += '('
    answer += solution(v)
    answer += ')'
    for c in u[1:len(u)-1]:
        if c == '(':
            answer += ')'
        else:
            answer += '('
    return answer