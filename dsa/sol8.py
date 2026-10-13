class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Step 1: Square all elements and sort them
        squares = sorted(x * x for x in nums)
        
        n = len(squares)
        m = n // 2
        
        # Step 2: Subtract the smallest squares and add the rest
        ans = 0
        for i in range(n):
            if i < m:
                ans -= squares[i]
            else:
                ans += squares[i]
                
        return ans
