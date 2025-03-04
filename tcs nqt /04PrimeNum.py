class Solution:
    def isPrime(self, n):
        # Handle edge cases
        if n <= 1:
            return False
        
        # Check for divisibility from 2 to square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True

# Example usage
sol = Solution()
print(sol.isPrime(2))   # True
print(sol.isPrime(17))  # True
print(sol.isPrime(4))   # False
pr
