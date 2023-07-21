def is_sorted(x, y):
    str1 = x + y
    str2 = y + x
    return str1 >= str2
    
def solution(numbers):
    answer = ''
    str_list = list(map(str, numbers))
    
    #flag = 0
    #while not flag:
    #    flag = True
    #    for i in range(len(str_list)-1):
    #        if not is_sorted(str_list[i], str_list[i+1]):
    #            str_list[i], str_list[i+1] = str_list[i+1], str_list[i]
    #            flag = False
    
    str_list.sort(key = lambda x: x*3, reverse = True)
    
    answer = "".join(str_list)
        
    if int(answer) == 0:
        return '0'
    
    return answer