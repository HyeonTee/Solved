#is_prime = [True] * 10000000
#is_prime[0] = is_prime[1] = False

#for num in range(2, int(10000000 ** 0.5) + 1):
#    if is_prime[num]:
#        for num_mul in range(num * num, 10000000, num):
#            is_prime[num_mul] = False

#prime_list = [i for i, is_prime in enumerate(is_prime) if is_prime]

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    else:
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
        return check

def make_num(num_list, num, depth, max_len):
    if depth == max_len:
        return
    for i in range(max_len):
        if not visited[i]:
            visited[i] = True
            check_list.append(num + num_list[i])
            make_num(num_list, num+num_list[i], depth+1, max_len)
            visited[i] = False

visited = [False] * 7
check_list = []

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    
    for i, number in enumerate(numbers):
        check_list.append(number)
        visited[i] = True
        make_num(num_list, number, 1, len(numbers))
        visited[i] = False
    
    int_list = list(set(map(int, check_list)))

    for i in int_list:
        if is_prime(i):
        #if i in prime_list:
            answer += 1
            
    return answer