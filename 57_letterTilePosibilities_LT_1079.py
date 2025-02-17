class Solution(object):  # Define a class named Solution.

    def numTilePossibilities(self, tiles):  
        """
        :type tiles: str  # Input: a string containing tile characters.
        :rtype: int       # Output: an integer representing the number of possible unique sequences of tiles.
        """

        from itertools import permutations  
        # Import the permutations function from itertools. 
        # It will allow us to generate all possible arrangements of the given tiles for a certain length.

        s = 0  
        # Initialize a variable `s` to 0. This will hold the total count of unique tile sequences.

        for i in range(1, len(tiles) + 1):  
            # Loop through lengths from 1 to the length of the input string `tiles`.
            # The `+1` ensures that all lengths (including maximum) are considered.

            p = permutations(tiles, i)  
            # Generate all permutations of length `i` from the `tiles` string.
            # This produces a list of tuples, representing all possible arrangements of the tiles of length `i`.

            s = s + len(list(set(p)))  
            # Convert `p` (the permutations object) to a set to remove duplicate permutations.
            # Then, convert it back to a list and calculate its length to count only unique permutations.
            # Add this count to `s`.

        return s  
        # Return the total count of all unique sequences of tiles from lengths 1 to `len(tiles)`.
