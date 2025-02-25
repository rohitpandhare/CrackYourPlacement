class Solution:
    def evenlyDivides(self, n):
        # Handle negative numbers
        original_n = abs(n)
        
        count = 0
        temp = original_n  # Copy of n for processing digits

        while temp != 0:
            digit = temp % 10  # Get the last digit
            temp //= 10  # Remove the last digit
            
            # Check if digit is not zero and evenly divides n
            if digit != 0 and original_n % digit == 0:
                count += 1
        
        return count
if __name__ == "__main__":
  n = 58964
  print(evenlyDivides(n))
