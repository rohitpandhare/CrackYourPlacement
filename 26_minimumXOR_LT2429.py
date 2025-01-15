class Solution(object):
    def minimizeXor(self, num1, num2):
        # Helper function to count number of set bits (1's) in a number
        def count_bits(n):
            res = 0
            while n > 0:
                res += 1 & n  # Add 1 if least significant bit is 1, 0 otherwise
                n = n >> 1    # Right shift to check next bit
            return res
        
        # Count set bits in both numbers
        cnt1 = count_bits(num1)  # Set bits in num1
        cnt2 = count_bits(num2)  # Set bits in num2
        
        x = num1  # Start with num1 as base
        i = 0     # Bit position counter
        
        # If num1 has more set bits than needed (cnt2)
        # Remove extra set bits from least significant positions
        while cnt1 > cnt2:
            if x & (1<<i):    # Check if current bit position is 1
                cnt1 -= 1     # Reduce count of set bits
                x = x ^ (1<<i)  # Flip the bit to 0 using XOR
            i += 1
        
        # If num1 has fewer set bits than needed (cnt2)
        # Add more set bits from least significant positions
        while cnt1 < cnt2:
            if x & (1<<i) == 0:  # Check if current bit position is 0
                cnt1 += 1        # Increase count of set bits
                x = x | (1<<i)   # Set the bit to 1 using OR
            i += 1
        
        return x
