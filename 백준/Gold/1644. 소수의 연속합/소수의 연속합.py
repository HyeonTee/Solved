import sys
input = sys.stdin.readline

n = int(input())

sieve = [True] * (n+1)
sieve[0] = False
sieve[1] = False
for i in range(2, int(n**0.5) + 1):
	for j in range(i*i, n+1, i):
		sieve[j] = False
		
primes = [i for i, n in enumerate(sieve) if n is True]

lt, rt, cnt, curr = 0, 0, 0, 0
while True:
	if curr >= n:
		curr -= primes[lt]
		lt += 1
	elif rt >= len(primes):
		break
	else:
		curr += primes[rt]
		rt += 1
	if curr == n:
		cnt += 1

print(cnt)