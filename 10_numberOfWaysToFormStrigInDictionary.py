#need more practice

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str] - List of words of equal length.
        :type target: str - Target string to form.
        :rtype: int - Number of ways to form the target string modulo 10^9 + 7.
        """
        MOD = 10**9 + 7  # Define the modulo value to avoid overflow.
      
        m, n = len(words), len(words[0])  # m: number of words, n: length of each word.
        t_len = len(target)  # Length of the target string.
      
        # Create a frequency table to count occurrences of each character at each position.
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for j, char in enumerate(word):
                freq[j][ord(char) - ord('a')] += 1  # Count frequency of each character.
              
        # Initialize a 2D dp array to store intermediate results.
        dp = [[0] * (n + 1) for _ in range(t_len + 1)]
        # Base case: There's one way to form an empty target string.
        dp[t_len][n] = 1
        # Fill the dp table from the bottom-up.
        for i in range(t_len, -1, -1):  # Iterate through target string from end to start.
            for j in range(n - 1, -1, -1):  # Iterate through positions in words from end to start.
                dp[i][j] = dp[i][j + 1]  # Option to skip the current column.
                # If not at the end of the target, consider using the current character.
                if i < t_len:
                    char_idx = ord(target[i]) - ord('a')  # Get the index of the character in 'a'-'z'.
                    # Add ways using the current character times ways from the next position.
                    dp[i][j] += freq[j][char_idx] * dp[i + 1][j + 1]
                    dp[i][j] %= MOD  # Take modulo to avoid overflow.
        # Return the number of ways to form the entire target string starting from position 0.
        return dp[0][0]
