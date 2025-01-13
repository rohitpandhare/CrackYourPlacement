class Solution(object):
    def minimumLength(self, s):
        freq = [0] * 26  # Create a list to store the frequency of each character
        for char in s:
            freq[ord(char) - ord('a')] += 1  # Increment the frequency of the character

        length = 0
        for count in freq:
            if count % 2 == 1:  # If the frequency is odd
                length += 1
            else:
                length += min(2, count)  # If the frequency is even, take the minimum of 2 and the frequency

        return length 
        
