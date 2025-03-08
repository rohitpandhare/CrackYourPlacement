class Solution:
    def sum_of_ap(self, n, a, d):
        # Validate input constraints
        if n <= 0:
            return 0
        
        # Calculate sum using closed-form AP formula
        # Sn = n/2 * [2a + (n-1)d]
        sum_ap = (n * (2 * a + (n - 1) * d)) // 2
        
        return sum_ap

# Driver code for testing
def main():
    # Create Solution object
    solution = Solution()
    
    # Test Case 1
    N = int(input())  # Number of terms
    A = int(input())  # First term
    D = int(input())  # Common difference
    
    # Call the method and print result
    result = solution.sum_of_ap(N, A, D)
    print(result)

# Standard boilerplate to call main function
if __name__ == "__main__":
    main()
