import sys
input = sys.stdin.readline

lt, rt = map(int, input().split())
MAX = int(rt ** 0.5) + 1

is_prime = [True] * (MAX + 1)
is_prime[0:2] = [False, False]
for i in range(2, int(MAX**0.5) + 1):
	if is_prime[i]:
		for j in range(i*i, MAX+1, i):
			is_prime[j] = False

primes = [i for i, v in enumerate(is_prime) if v]

length = rt - lt + 1
result = [1] * length

for prime in primes:
	square = prime ** 2
	if square > rt:
		break

	start = ((lt + square - 1) // square) * square
	for curr in range(start, rt + 1, square):
		result[curr - lt] = 0

print(sum(result))