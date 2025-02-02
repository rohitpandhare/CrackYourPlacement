class Solution(object):
    def check(self, nums):
        n = len(nums)          # Get the length of the array
        count = 1              # Initialize a counter to track consecutive non-decreasing elements

        if n == 1:
            return True        # An array with a single element is always considered sorted

        # Iterate through the array twice to simulate a circular array
        for i in range(1, 2 * n):
            # Compare the current element with the previous one using modulo for circular indexing
            if nums[(i - 1) % n] <= nums[i % n]:
                count += 1      # Increment the counter if the current pair is non-decreasing
            else:
                count = 1       # Reset the counter if the sequence is broken

            # If the counter reaches the length of the array, it's sorted in a rotated manner
            if count == n:
                return True

        # If no such sequence is found after the complete iteration, return False
        return False
