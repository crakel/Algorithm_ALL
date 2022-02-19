import sys


def binary_search(value, list, visit):
    start = 0
    end = len(list) - 1

    while start <= end:
        visit += 1
        mid = (start + end) // 2

        if list[mid] == value:
            return visit
        elif list[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return


odd = []
even = []

for i in range(1, 101):
    if i % 2 ==  1:
        odd.append(i)

    else:
        even.append(i)

while True:
    visit = 0
    cur_index = 24

    shop = int(sys.stdin.readline())

    if shop == 0:
        break

    else:
        if shop not in even:
            visit += 1 # 홀수 블록으로 넘어온다
            visit = binary_search(shop, odd, visit)
            print(visit)

        else:
            visit = binary_search(shop, even, visit)
            print(visit)