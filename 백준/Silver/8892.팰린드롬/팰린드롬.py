import sys


def check_palindrome(s: list) -> bool:
    while len(s) > 1:
        if s.pop(0) != s.pop():
            return False
    return True


T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    note = []
    for __ in range(k):
        note.append(sys.stdin.readline().strip())

    flag = False
    for i in range(len(note)):
        if flag:
            break
        for j in range(len(note)):
            if i == j:
                continue
            if check_palindrome(list((note[i] + note[j]))):
                print(note[i] + note[j])
                flag = True
                break

    if not flag:
        print(0)