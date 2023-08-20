class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if first >= num:
                first = num
            elif second >= num:
                second = num
            else:
                return True
        
        return False