def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    res_1 = ''
    for c in new_id:
        if c.isalnum() or c in ('-', '_', '.'):
            res_1 += c

    # 3단계
    res_2 = ''
    cnt = 0
    for c in res_1:
        if c == '.':
            cnt += 1
            continue
        elif c != '.' and cnt:
            cnt = 0
            res_2 += '.'
        res_2 += c

    # 4단계
    if len(res_2) and res_2[0] == '.':
        res_2 = res_2[1:]
    if len(res_2) and res_2[-1] == '.':
        res_2 = res_2[:len(res_2)-1]

    # 5단계
    if not len(res_2):
        res_2 = 'a'
    # 6단계
    print(res_2)
    if len(res_2) >= 16:
        res_2 = res_2[:15]
        print(res_2)
        if res_2[-1] == '.':
            res_2 = res_2[:len(res_2)-1]
    print(res_2)

    # 7단계
    if len(res_2) <= 2:
        lc = res_2[-1]
        while len(res_2) < 3:
            res_2 += lc

    return res_2