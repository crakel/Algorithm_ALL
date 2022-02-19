m, n = map(int, input().split())

is_prime = [ False, False ] + [ True ] * (n-1)
primes = []

for i in range(2, n+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*2, n+1, i):
            is_prime[j] = False

for x in primes:
    if x >= m:
        print(x)