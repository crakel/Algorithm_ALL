n = int(input())
member = []

for i in range(n):
    member.append(input().split())

member = sorted(member, key = lambda x: int(x[0]))

for x in member:
    print(x[0], x[1])