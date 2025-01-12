class Solution(object):
    def canBeValid(self, s, locked):
        n = len(s)
        
        # If the length is odd, it's impossible to form a valid parentheses string
        if n % 2 != 0:
            return False
        
        a, b = 0, 0  # Initialize counts for '(' and ')'
        
        # Forward pass: Ensure we don't have excess ')'
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                a += 1  # Treat unlocked or '(' as '('
            else:
                b += 1  # Count closing parentheses
            if b > a:  # If closing exceeds opening, not valid
                return False
        
        a, b = 0, 0  # Reset counts for backward pass
        
        # Backward pass: Ensure we don't have excess '('
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                b += 1  # Treat unlocked or ')' as ')'
            else:
                a += 1  # Count opening parentheses
            if a > b:  # If opening exceeds closing, not valid
                return False
        
        return True
