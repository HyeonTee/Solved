class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        candyMax = max(candies)
        result = [False] * n
        
        for i in range(n):
            if (candies[i] + extraCandies) >= candyMax:
                result[i] = True
        
        return result