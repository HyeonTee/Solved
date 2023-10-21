import sys
input = sys.stdin.readline

limit = 1000000
primes = set()
sieve = [False, False] + [True] * (limit - 1)

for i in range(2, int(limit ** 0.5) + 1):
	if sieve[i]:
		for j in range(i*2, limit, i):
			sieve[j] = False

for i in range(limit + 1):
	if sieve[i]:
		primes.add(i)

while True:
	num = int(input())
	if num == 0:
		break

	lt = 3
	rt = num - 3
	while True:
		if lt in primes and rt in primes:
			print(num , "=" , lt , "+" , rt)
			break
		else:
			lt += 2
			rt -= 2