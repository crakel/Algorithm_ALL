import sys
t = int(sys.stdin.readline())

for i in range(t):
    func = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip().strip('[]').split(',')
    func = func.replace('RR', '') # R연속 2번은 제거

    r = 0
    del_front = 0
    del_back = 0

    for x in func:
        if x == 'R':
            r += 1

        elif x == 'D':
            if r % 2 == 0: # r이 짝수이면 앞에서 제거
                del_front += 1

            else:
                del_back += 1

    del_sum = del_front + del_back

    if del_sum > n: # 지워야 할게 리스트 크기보다 많다면
        print("error")

    else:
        for j in range(del_sum):
            if del_front > 0:
                del arr[0]
                del_front -= 1

            if del_back > 0:
                del arr[-1]
                del_back -= 1

        if r % 2 == 0: # r이 짝수일 때 그대로 출력
            print('[' + ','.join(arr) +']')

        else:
            print('[' + ','.join(arr[::-1]) + ']')