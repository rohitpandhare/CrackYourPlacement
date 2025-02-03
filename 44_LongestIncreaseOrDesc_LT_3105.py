class Solution(object):
    def longestMonotonicSubarray(self, nums):
        # Check if the input list is empty.
        # If it is, there's no subarray to consider, so return 0.
        if not nums:
            return 0

        # Initialize 'current' to 1 since a single element is a valid monotonic subarray.
        current = 1

        # 'result' will store the length of the longest monotonic subarray found.
        # Initialize it to 1 for the same reason as 'current'.
        result = 1

        # 'increasing' is a flag to indicate the current trend of the subarray.
        # 1 means the subarray is currently increasing,
        # -1 means it's decreasing,
        # and 0 means there's no current trend (e.g., elements are equal).
        increasing = 0

        # Iterate through the list starting from the second element.
        for i in range(1, len(nums)):
            # Check if the current element is greater than the previous one.
            if nums[i-1] < nums[i]:
                # If the previous trend was increasing,
                # extend the current subarray by incrementing 'current'.
                if increasing > 0:
                    current += 1
                else:
                    # If the previous trend was not increasing,
                    # start a new subarray of length 2 (current and previous elements).
                    current = 2
                    # Update the trend to increasing.
                    increasing = 1

            # Check if the current element is less than the previous one.
            elif nums[i-1] > nums[i]:
                # If the previous trend was decreasing,
                # extend the current subarray by incrementing 'current'.
                if increasing < 0:
                    current += 1
                else:
                    # If the previous trend was not decreasing,
                    # start a new subarray of length 2 (current and previous elements).
                    current = 2
                    # Update the trend to decreasing.
                    increasing = -1

            else:
                # If the current and previous elements are equal,
                # reset the current subarray length to 1.
                current = 1
                # Reset the trend since equal elements break monotonicity.
                increasing = 0

            # Update 'result' if the current subarray is longer than the previously recorded maximum.
            result = max(result, current)

        # After iterating through the list, return the length of the longest monotonic subarray found.
        return result
