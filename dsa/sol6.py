class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Step 1: Calculate absolute differences
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        
        # If total operations can reduce all differences to 0
        if sum(diff) <= total_k:
            return 0
            
        # Step 2: Count frequencies of each difference
        max_val = max(diff)
        count = [0] * (max_val + 2)
        for d in diff:
            count[d] += 1
            
        # Step 3: Greedily reduce the largest differences using bucket/frequency sweep
        k = total_k
        for i in range(max_val, 0, -1):
            if count[i] > 0:
                reduce_amt = min(k, count[i])
                count[i] -= reduce_amt
                count[i - 1] += reduce_amt
                k -= reduce_amt
                if k == 0:
                    break
                    
        # Step 4: Calculate final sum of squared differences
        ans = 0
        for i in range(max_val + 1):
            if count[i] > 0:
                ans += count[i] * (i * i)
                
        return ans
