class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [0] * n
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 != 0:
                ans[i-1] = "Fizz"
            elif i % 3 != 0 and i % 5 == 0:
                ans[i-1] = "Buzz"
            elif i % 15 == 0:
                ans[i-1] = "FizzBuzz"
            else:
                ans[i-1] = str(i)
        
        return ans