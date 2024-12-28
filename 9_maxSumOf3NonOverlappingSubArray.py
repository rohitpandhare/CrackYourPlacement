#hard - need to loop for better approach

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        # Initialize the array to store the sum of each window of size `k`.
        k_sums = [sum(nums[:k])]  # First window sum

        # Calculate k_sums for all windows of size `k` in nums
        for i in range(k, len(nums)):  # From the k-th index to the last index
            # Update the k_sums array with rolling window sums
            k_sums.append(k_sums[-1] + nums[i] - nums[i - k])  
            # The new sum is the previous window sum + current element - element that slides out of the window
        
        # Dynamic programming dictionary to store solutions of overlapping subproblems
        dp = {}

        # Helper function to calculate the maximum sum with recursion and memoization
        def get_max_sum(i, count):
            # If we already chose 3 subarrays or reached out of bounds, return 0
            if (count == 3) or (i > len(nums) - k):  
                return 0

            # If the result for this state is already computed, return it
            if (i, count) in dp:
                return dp[(i, count)]

            # Include the current window
            include = k_sums[i] + get_max_sum(i + k, count + 1)
            # Skip the current window
            skip = get_max_sum(i + 1, count)

            # Store the maximum of include or skip in the dp dictionary
            dp[(i, count)] = max(include, skip)

            return dp[(i, count)]

        # Function to retrieve the indices of the three subarrays
        def get_indices():
            i = 0
            indices = []

            # Continue iterating until we reach the end of the array or collect 3 indices
            while (i <= len(nums) - k) and (len(indices) < 3):
                # Include the current window
                include = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
                # Skip the current window
                skip = get_max_sum(i + 1, len(indices))

                # Decide whether to include or skip based on the max value
                if include >= skip:
                    indices.append(i)
                    i += k  # Move forward by k when including
                else:
                    i += 1  # Move to the next index when skipping

            return indices

        # Call the `get_indices` method to obtain the result
        return get_indices()
