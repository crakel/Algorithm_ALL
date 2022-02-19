n = input()
count = 0

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0

for i in range(len(cro)):
    if n.count(cro[i]) > 0:
        count += n.count(cro[i])
        n = n.replace(cro[i], ' ')

for x in n:
    if x != ' ':
        count += 1

print(count)