class Solution(object):
    def getHappyString(self, n, k):
        # Check if k is larger than possible number of happy strings
        # For length n, each position has 2 choices except first (which has 3)
        # So total possible strings = 3 * 2^(n-1)
        if k > 3 * (1 << (n - 1)):  # 1 << (n-1) is same as 2^(n-1)
            return ""
        
        # Decrease k by 1 to convert to 0-based indexing
        k -= 1
        
        # Initialize result array and mapping for next valid characters
        res = []
        # Dictionary showing which characters can follow each character
        next_char = {
            'a': 'bc',  # After 'a', either 'b' or 'c' can come
            'b': 'ac',  # After 'b', either 'a' or 'c' can come
            'c': 'ab'   # After 'c', either 'a' or 'b' can come
        }
        
        # Generate string character by character
        for i in range(n):
            if i == 0:
                # For first character
                # k >> (n-i-1) gives the index of first character (0,1,2)
                # 'abc'[index] selects 'a', 'b', or 'c'
                res.append('abc'[k >> (n - i - 1)])
            else:
                # For subsequent characters
                # Get valid next characters from next_char dictionary
                # (k >> (n-i-1)) & 1 gives 0 or 1 to select from valid chars
                res.append(next_char[res[-1]][(k >> (n - i - 1)) & 1])
        
        # Join characters and return final string
        return "".join(res)
