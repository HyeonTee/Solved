from itertools import combinations

while True:
    test = list(map(int, input().split()))
    if test[0] == 0:
        break
    
    S = test[1:]

    for comb in combinations(S, 6):
        print(*comb)
    
    print()