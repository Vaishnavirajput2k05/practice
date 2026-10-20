class Solution:
    def sumOfSortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0
        
        # Step 2: Check each divisor k
        for k in divisors:
            sortable = True
            prev_max = -float('inf')
            
            for i in range(0, n, k):
                block = nums[i : i + k]
                
                # Check if the block has at most 1 circular descent
                drops = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1
                if drops > 1:
                    sortable = False
                    break
                
                block_min = min(block)
                block_max = max(block)
                
                # Check inter-block ordering
                if block_min < prev_max:
                    sortable = False
                    break
                
                prev_max = block_max
                
            if sortable:
                total_sum += k
                
        return total_sum
