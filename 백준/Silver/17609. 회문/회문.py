import sys

t = int(sys.stdin.readline())


def is_pal(s: str):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            if left < right - 1:
                tmp = s[:right] + s[right+1:]
                if tmp == tmp[::-1]:
                    return 1

            if left + 1 < right:
                tmp = s[:left] + s[left+1:]
                if tmp == tmp[::-1]:
                    return 1

            return 2
    return 0


# 투 포인터 사용
for _ in range(t):
    print(is_pal(sys.stdin.readline().rstrip()))

# 단순 구현 -> 시간초과
# def is_ps_palin(s: str):
#     for i in range(len(s)):
#         new_s = list(s)
#         del new_s[i]
#         if new_s == new_s[::-1]:
#             return True
#     return False
#
#
# for _ in range(t):
#     s = sys.stdin.readline().rstrip()
#     if s == s[::-1]:
#         print(0)
#
#     else:
#         if is_ps_palin(s):
#             print(1)
#         else:
#             print(2)
