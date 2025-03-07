class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Handle edge cases
        if n <= 0:
            return 0
        
        # Optimize for small values
        if n == 1 or n == 2:
            return 1
        
        # Dynamic programming approach for efficiency
        # Initialize the first two Fibonacci numbers
        fib = [0] * (n + 1)
        fib[1] = 1
        fib[2] = 1
        
        # Calculate Fibonacci numbers iteratively
        for i in range(3, n + 1):
            fib[i] = fib[i-1] + fib[i-2]
        
        # Return the nth Fibonacci number
        return fib[n]

# Example usage
solution = Solution()
print(solution.nthFibonacci(10))  # Will print the 10th Fibonacci number


""""
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n <= 0:
            return 0
        
        elif n == 1 or n ==2:
            return 1
        
        else:
            return self.nthFibonacci(n-1) + self.nthFibonacci(n-2) 
""""
