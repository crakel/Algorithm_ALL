import sys

n = int(sys.stdin.readline())
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
serial = []

def sum_digit(serial):
    res = 0
    for x in serial:
        if x in num:
           res += int(x)
    return res

for _ in range(n):
    serial.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(i+1, n):
        if len(serial[i]) > len(serial[j]):
            serial[i], serial[j] = serial[j], serial[i]

        elif len(serial[i]) == len(serial[j]):
            if sum_digit(serial[i]) > sum_digit(serial[j]):
                serial[i], serial[j] = serial[j], serial[i]

            elif sum_digit(serial[i]) == sum_digit(serial[j]):
                if serial[i] > serial[j]:
                    serial[i], serial[j] = serial[j], serial[i]


for x in serial:
    print(x)