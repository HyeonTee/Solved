N = int(input())
K = 2**N - 1

def hanoi(n, start, to, auxi):
    if n == 1:
        print(start, to)
        return

    hanoi(n-1, start, auxi, to)
    print(start, to)
    hanoi(n-1, auxi, to, start)

print(K)
hanoi(N, 1, 3, 2)