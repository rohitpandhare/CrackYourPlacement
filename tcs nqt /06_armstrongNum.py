class Solution:
    # count the number of digits in number
    def order(self, n):
        if n == 0:
            return 1
        
        count = 0
        while n:
            count += 1
            n //= 10
        return count

    # count the powers
    def power(self, x, y):
        return x ** y
        
    def armstrongNumber(self, n):
        # code here 
        temp = n
        o = self.order(n)
        
        sum1 = 0
        
        while temp:
            r = temp % 10
            sum1 += self.power(r, o)
            temp //= 10
            
        return sum1 == n

# TCS NQT Test Case Handler
def main():
    # Read number of test cases
    T = int(input())
    
    # Solution object
    solution = Solution()
    
    # Process each test case
    for _ in range(T):
        # Read input number
        N = int(input())
        
        # Check if Armstrong number and print result
        if solution.armstrongNumber(N):
            print("Yes")
        else:
            print("No")

# Run the main function
if __name__ == "__main__":
    main()

# Sample Test Case Input Format:
# 4           # Number of test cases
# 153         # First number
# 370         # Second number
# 371         # Third number
# 407         # Fourth number

# Expected Output:
# Yes
# Yes
# Yes
# Yes
