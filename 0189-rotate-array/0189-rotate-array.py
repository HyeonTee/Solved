class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr, lt, rt):
            while lt <= rt:
                arr[lt], arr[rt] = arr[rt], arr[lt]
                lt += 1
                rt -= 1
        
        n = len(nums)
        k %= n
        
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)