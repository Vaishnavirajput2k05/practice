class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Helper function to compute digit sum
        def get_digit_sum(num: int) -> int:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        # Pair each number with its value, digit sum, and original index
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((get_digit_sum(num), num, i))
            
        # Sort based on digit sum first, then numerical value
        indexed_nums.sort(key=lambda x: (x[0], x[1]))
        
        # Find minimum swaps using cycle detection
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or indexed_nums[i][2] == i:
                continue
                
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1
                
            # If a cycle of length k is found, it requires (k - 1) swaps
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
