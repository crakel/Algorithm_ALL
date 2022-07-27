def rotate(key):
    return list(zip(*key[::-1]))

def key_on(x, y, M, key, field):
    for i in range(M):
        for j in range(M):
            field[x+i][y+j] += key[i][j]

def key_off(x, y, M, key, field):
    for i in range(M):
        for j in range(M):
            field[x+i][y+j] -= key[i][j]

def check(field, M, N):
    for i in range(N):
        for j in range(N):
            if field[M+i][M+j] != 1:
                return False;
    return True         

def solution(key, lock):
    M, N = len(key), len(lock)
    field = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    
    rotate_key = key[:]
    
    for i in range(N):
        for j in range(N):
            field[M+i][M+j] = lock[i][j]
    
    for _ in range(4):
        rotate_key = rotate(rotate_key)
        print(rotate_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                key_on(x, y, M, rotate_key, field)
                #print(check(field, M, N))
                if(check(field, M, N)):
                    return True
                key_off(x, y, M, rotate_key, field)
    return False