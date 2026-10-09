class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_needed += 1
                i += 1
            else:  # s[i] == ')'
                # Check if it's a double closing parenthesis "))"
                if i + 1 < n and s[i + 1] == ')':
                    if open_needed > 0:
                        open_needed -= 1
                    else:
                        insertions += 1  # Need '('
                    i += 2  # Consumed both ')'
                else:  # Single ')'
                    insertions += 1  # Need one more ')' to form "))"
                    if open_needed > 0:
                        open_needed -= 1
                    else:
                        insertions += 1  # Need '('
                    i += 1  # Consumed single ')'
                    
        # Any remaining unmatched '(' needs '))' (2 closing per open)
        insertions += open_needed * 2
        return insertions
