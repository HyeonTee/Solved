class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100001
        profit = 0
        
        for price in prices:
            if price - min_price > profit:
                profit = price - min_price
                
            if min_price > price:
                min_price = price
        
        return profit