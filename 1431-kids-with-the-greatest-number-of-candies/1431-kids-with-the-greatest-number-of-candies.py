class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyMax = max(candies)
        result = []
        
        for candy in candies:
            if (candy + extraCandies) >= candyMax:
                result.append(True)
            else:
                result.append(False)
        
        return result