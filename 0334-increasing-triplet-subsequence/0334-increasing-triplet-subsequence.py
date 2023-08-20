class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if first >= num: # 가장 작은 수
                first = num
            elif second >= num: # 두번째로 작은 수
                second = num
            else: # 세번째로 작은 수 존재하는 경우
                return True
        
        return False