class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if already sorted
        if all(s[i] <= s[i+1] for i in range(n - 1)):
            return 0
            
        # If length is 2 and not sorted, it's impossible
        if n == 2:
            return -1
            
        mn, mx = min(s), max(s)
        
        # If min is at the start or max is at the end
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # If min or max is in the interior proper substring
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
                
        return 3
