class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lt = 0
        rt = n-1
        max_area = 0
        while lt <= rt:
            new_area = min(height[lt], height[rt]) * (rt-lt)
            max_area = max(max_area, new_area)
            if height[lt] > height[rt]:
                rt -= 1
            else:
                lt += 1
                
        return max_area