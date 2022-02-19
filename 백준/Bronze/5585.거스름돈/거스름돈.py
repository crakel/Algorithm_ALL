n = int(input())

back = 1000 - n
count = 0
while back > 0:
    if back >= 500:
        count += 1
        back -= 500

    elif back >= 100 and back < 500:
        count += 1
        back -= 100

    elif back >= 50 and back < 100:
        count += 1
        back -= 50

    elif back >= 10 and back < 50:
        count += 1
        back -= 10

    elif back >= 5 and back < 10:
        count += 1
        back -= 5

    else:
        count += 1
        back -= 1

print(count)