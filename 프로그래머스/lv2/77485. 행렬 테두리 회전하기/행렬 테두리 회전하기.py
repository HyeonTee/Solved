def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns+1) for _ in range(rows+1)]
    
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            matrix[i][j] = (i-1)*columns + j
    
    for x1, y1, x2, y2 in queries:
        rotate_index = []
        rotate_list = []
        for i in range(y1, y2):
            rotate_index.append((x1, i))
            rotate_list.append(matrix[x1][i])
        for i in range(x1, x2):
            rotate_index.append((i, y2))
            rotate_list.append(matrix[i][y2])
        for i in range(y2, y1, -1):
            rotate_index.append((x2, i))
            rotate_list.append(matrix[x2][i])
        for i in range(x2, x1, -1):
            rotate_index.append((i, y1))
            rotate_list.append(matrix[i][y1])
        
        temp = [rotate_list[-1]]
        rotate_list = rotate_list[:-1]
        rotate_list = temp + rotate_list
        
        answer.append(min(rotate_list))
        
        for i in range(len(rotate_index)):
            matrix[rotate_index[i][0]][rotate_index[i][1]] = rotate_list[i]
        
    return answer