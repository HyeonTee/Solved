def recur(numbers, target, i, num_sum):
    global answer
    if i == len(numbers):
        if num_sum == target:
            answer += 1
        return
    
    recur(numbers, target, i+1, num_sum + numbers[i])
    recur(numbers, target, i+1, num_sum - numbers[i])

def solution(numbers, target):
    global answer
    answer = 0

    recur(numbers, target, 0, 0)
    
    return answer