class Solution:
    def maximumScore(self, num: int, sum: int) -> str:
        # If the required sum exceeds the maximum possible sum for 'num' digits
        if sum > 9 * num:
            return ""
        
        q = sum // 9
        r = sum % 9
        
        # If we can fill all digits with 9s
        if q == num:
            return "9" * num
            
        # Construct the largest possible number: q nines, remainder r, and trailing zeros
        nines = "9" * q
        rem = str(r) if r > 0 else ""
        zeros = "0" * (num - q - (1 if r > 0 else 0))
        
        return nines + rem + zeros
