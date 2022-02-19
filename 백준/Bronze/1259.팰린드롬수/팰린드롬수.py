import sys


def check_palindrome(s: list) -> bool:
    while len(s) > 1:
        if s.pop(0) != s.pop():
            return False
    return True


while True:
    n = list(map(str, sys.stdin.readline().strip()))
    if n[0] == '0':
        exit(0)

    if check_palindrome(n):
        print('yes')
    else:
        print('no')
