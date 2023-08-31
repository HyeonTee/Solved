# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lt = 1
        rt = n
        
        while lt <= rt:
            mid = (lt + rt) // 2
            if guess(mid) == 1:
                lt = mid + 1
            elif guess(mid) == -1:
                rt = mid - 1
            else:
                return mid
        
        return mid