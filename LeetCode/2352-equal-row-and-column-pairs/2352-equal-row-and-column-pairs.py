class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt = 0
        
        columns = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                columns[j].append(grid[i][j])
        
        for i in range(n):
            for j in range(n):
                if grid[i] == columns[j]:
                    cnt += 1
        
        return cnt