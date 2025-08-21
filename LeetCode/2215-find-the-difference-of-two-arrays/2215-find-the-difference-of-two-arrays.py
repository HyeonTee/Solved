class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numset1 = set(nums1)
        numset2 = set(nums2)
        
        ans1 = list(numset1 - numset2)
        ans2 = list(numset2 - numset1)
        
        return [ans1, ans2]