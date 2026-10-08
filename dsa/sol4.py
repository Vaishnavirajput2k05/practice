class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        
        for char in s:
            if char == '(':
                # If balance > 0, this '(' is NOT an outermost parenthesis
                if balance > 0:
                    result.append(char)
                balance += 1
            else:  # char == ')'
                balance -= 1
                # If balance > 0 after decrementing, this ')' is NOT an outermost parenthesis
                if balance > 0:
                    result.append(char)
                    
        return "".join(result)
