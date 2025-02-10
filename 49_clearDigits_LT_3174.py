class Solution(object):  
    def clearDigits(self, s):
        res = ""  # Initialize an empty string to store the result.

        for c in s:  # Loop through each character in the input string `s`.
            if c.isdigit():  # Check if the current character `c` is a digit (0-9).
                if res:  # If `res` is not empty:
                    res = res[:-1]  # Remove the last character from `res`.
            else:  # If the current character `c` is NOT a digit:
                res += c  # Append `c` to the result string `res`.

        return res  # Once the loop is finished, return the final string `res`.
