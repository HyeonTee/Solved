def solution(park, routes):
    height = len(park)
    width = len(park[0])
    
    for i in range(height):
        for j in range(width):
            if park[i][j] == "S":
                x = i
                y = j

    def is_valid(x, y):
        if x < 0 or y < 0 or x >= height or y >= width:
            return False
        return True
    
    dir_dict = {"E": 0, "N": 1, "W": 2, "S": 3}
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for route in routes:
        direction = dir_dict[route[0]]
        dist = int(route[-1])
        
        ok = True
        for i in range(1, dist + 1):
            nx = x + dx[direction] * i
            ny = y + dy[direction] * i
            if not is_valid(nx, ny) or park[nx][ny] == "X":
                ok = False
                break
        if ok:
            x += dx[direction] * dist
            y += dy[direction] * dist
    
    return [x, y]