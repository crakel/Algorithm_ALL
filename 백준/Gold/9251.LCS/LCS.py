import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

len1 = len(str1)
len2 = len(str2)

# 가로 세로 0인 부분 추가
t = [[0] * (len1+1) for _ in range(len2+1)]

for i in range(1, len2+1):
    for j in range(1, len1+1):
        if str2[i - 1] == str1[j -1]:
            t[i][j] = t[i-1][j-1] + 1 # 문자 같으면 대각선 값 + 1

        else:
            t[i][j] = max(t[i-1][j], t[i][j-1]) # 아니라면 위,왼 중 큰값

print(t[-1][-1])