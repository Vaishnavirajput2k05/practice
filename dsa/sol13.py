import sys

# Increase recursion depth for skewed trees (up to 1000 depth)
sys.setrecursionlimit(2000)

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute Pascal's triangle for binomial coefficients C(n, k)
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
                
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            ways_left = dfs(left)
            ways_right = dfs(right)
            
            l_len = len(left)
            r_len = len(right)
            
            # Combine combinations and subtree ways modulo 10^9 + 7
            interleave_ways = comb[l_len + r_len][l_len]
            return interleave_ways * ways_left % MOD * ways_right % MOD

        # Subtract 1 because the original array itself is counted in the total
        return (dfs(nums) - 1 + MOD) % MOD
