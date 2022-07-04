import math

def solution(n, k):
    answer = 0
    
    def convert(n, k):
        res = ""
        
        while n > 0:
            n, mod = divmod(n, k)
            res += str(mod)
        return res[::-1]
    
    def is_prime(n):
        if n < 2:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
        return True

    #print(convert(n,k))
    lst = list(convert(n,k).split('0'))
    
    for n in lst:
        if n and is_prime(int(n)):
            answer += 1
    return answer