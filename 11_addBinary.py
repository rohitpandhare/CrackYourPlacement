class Solution(object):
    def addBinary(self, a, b):
        """
        Adds two binary strings and returns their sum as a binary string.
        
        :type a: str  # First binary number as a string
        :type b: str  # Second binary number as a string
        :rtype: str   # Sum of the two binary numbers as a binary string
        """
        # Initialize carry to handle overflow during addition
        carry = 0
        # Initialize an empty string for result
        result = ''

        # Convert the input strings to lists for easy manipulation (e.g., popping elements)
        a = list(a)
        b = list(b)

        # Continue looping as long as there are digits to process in a or b, or there's a carry-over
        while a or b or carry:
            # If there are remaining digits in 'a', pop the last digit and add its integer value to carry
            if a:
                carry += int(a.pop())
            
            # If there are remaining digits in 'b', pop the last digit and add its integer value to carry
            if b:
                carry += int(b.pop())

            # Determine the next binary digit to add to the result
            # carry % 2 gives the current bit (0 or 1)
            result += str(carry % 2)
            
            # Update carry for the next iteration
            # carry //= 2 effectively shifts the carry to the next higher bit
            carry //= 2

        # The result is built in reverse order (from least significant bit to most), so reverse it before returning
        return result[::-1]
