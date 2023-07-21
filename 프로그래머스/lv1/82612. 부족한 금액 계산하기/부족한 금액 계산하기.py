def solution(price, money, count):
    price_sum = 0
    for i in range(count+1):
        price_sum += i * price
    if price_sum > money:
        answer = price_sum - money
    else: answer = 0

    return answer