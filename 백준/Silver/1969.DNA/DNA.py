import sys

n, m = map(int, sys.stdin.readline().split())

dna = []
sum_hamdist = 0
res = []

for i in range(n):
    dna.append(sys.stdin.readline().strip())

for i in range(m):
    dna_count = [0, 0, 0, 0]  # A C G T (사전 순)
    for j in range(n):
        x = dna[j][i]
        if x == 'A':
            dna_count[0] += 1
        elif x == 'C':
            dna_count[1] += 1
        elif x == 'G':
            dna_count[2] += 1
        elif x == 'T':
            dna_count[3] += 1

        max_match = dna_count.index(max(dna_count))

    if max_match == 0:
        res.append('A')
    elif max_match == 1:
        res.append('C')
    elif max_match == 2:
        res.append('G')
    elif max_match == 3:
        res.append('T')

    sum_hamdist += n - max(dna_count)

print(''.join(res))
print(sum_hamdist)