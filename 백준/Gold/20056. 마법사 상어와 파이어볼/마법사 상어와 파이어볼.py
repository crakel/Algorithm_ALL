import sys
from collections import defaultdict
N, M, K = map(int, sys.stdin.readline().split())

D = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#        ↑        ↗       →       ↘       ↓       ↙        ←         ↖

infos = []
fb = defaultdict(list)
trash = []
for _ in range(M):
    infos.append(list(map(int, sys.stdin.readline().split())))

for info in infos:
    r, c, m, s, d = info
    fb[(r-1, c-1)] = [[m, s, d]]

for _ in range(K):
    # 이동
    move_fb = defaultdict(list)
    for key, value in list(fb.items()):
        r, c = key
        for v in value:
            m, s, d = v
            move = ((r + D[d][0] * s) % N, (c + D[d][1] * s) % N)
            move_fb[move].append([m, s, d])
            # if move in move_fb:
            #     move_fb[move].append([m, s, d])
            # else:
            #     move_fb[move] = [[m, s, d]]
        # while value:
        #     m, s, d = value.pop(0)
        #     move = ((r + D[d][0] * s) % N, (c + D[d][1] * s) % N)
        #     if move in fb:
        #         move_fb[move].append([m, s, d])
        #     else:
        #         move_fb[move] = [[m, s, d]]
    # print(fb)
    # print(move_fb)
    fb = move_fb

    # 2개이상 발생
    for key, value in fb.items():
        if len(value) >= 2:
            m = 0
            s = 0
            even_cnt = 0
            odd_cnt = 0
            for v in value:
                m += v[0]
                s += v[1]
                if v[2] % 2 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1
            m //= 5
            s //= len(value)
            fb[key] = []
            if m != 0:
                if even_cnt == len(value) or odd_cnt == len(value):
                    for i in [0, 2, 4, 6]:
                        fb[key].append([m, s, i])
                else:
                    for i in [1, 3, 5, 7]:
                        fb[key].append([m, s, i])
            # else:
            #     trash.append(key)
    # for t in trash:
    #     del fb[t]

# print(fb)
m_sum = 0
for value in fb.values():
    for v in value:
        m_sum += v[0]
print(m_sum)