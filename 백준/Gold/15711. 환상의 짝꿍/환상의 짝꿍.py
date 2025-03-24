import sys
input = sys.stdin.readline

MAX = 2000000

def sieve(limit):
	is_prime = [True] * (limit + 1)
	is_prime[0:2] = [False, False]
	for i in range(2, int(limit**0.5) + 1):
		if is_prime[i]:
			for j in range(i*i, limit+1, i):
				is_prime[j] = False

	primes = [i for i, v in enumerate(is_prime) if v]
	return primes, is_prime

primes, is_prime = sieve(MAX+1)

def is_tied(num):
	if num <= 3:
		return False
	if (num & 1) == 0:
		return True
	if num <= MAX:
		if is_prime[num - 2]:
			return True
	else:
		for prime in primes:
			if (num - 2) % prime == 0:
				return False
		return True

T = int(input())
for _ in range(T):
	a, b = map(int, input().split())
	s = a + b
	if (is_tied(s)):
		print("YES")
	else:
		print("NO")