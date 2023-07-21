T = int(input())

def is_prime(n):
    result = 1
    if n != 2:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                result = 0
    return result
for _ in range(T):
    n = int(input())
    a = b = n//2
    while True:
        if is_prime(a) + is_prime(b) == 2:
            break
        a -= 1
        b += 1

    print(a, b) 