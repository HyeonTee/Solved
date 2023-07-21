import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    
    dp_table = [0] * (money + 1)
    dp_table[0] = 1
    for coin in coins:
        for i in range(coin, money+1):
            if dp_table[i-coin] > 0:
                dp_table[i] = dp_table[i-coin] + dp_table[i]
    
    print(dp_table[money])