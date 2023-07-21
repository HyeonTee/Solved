def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"{source} {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"{source} {target}")
    hanoi(n-1, auxiliary, target, source)

n = int(input())
if n <= 20:
    print(2**n-1)
    hanoi(n, 1, 3, 2)
else:
    print(2**n-1)