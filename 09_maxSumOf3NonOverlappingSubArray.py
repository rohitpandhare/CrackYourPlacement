#hard - need to loop for better approach
'''
# optimal
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        # Get the length of the input array
        n = len(nums)
        
        # Calculate the initial sums of the first three subarrays of length k
        sum1 = sum(nums[:k])          # Sum of the first subarray
        sum2 = sum(nums[k:2 * k])       # Sum of the second subarray
        sum3 = sum(nums[2*k:3 * k])     # Sum of the third subarray

        # Initialize maximum sums for the first, first two, and all three subarrays
        max1 = sum1                   # Maximum sum of the first subarray
        max12 = sum1 + sum2           # Maximum sum of the first two subarrays
        max123 = sum1 + sum2 + sum3   # Maximum sum of all three subarrays

        # Initialize indices to track the starting points of the subarrays
        index1 = 0                     # Starting index of the first subarray
        index12_1 = 0                  # Starting index of the first subarray in the first two
        index12_2 = k                  # Ending index of the second subarray in the first two
        ans = [0, k, 2 * k]            # To store the best indices of the three subarrays

        # Iterate through the array to find the best subarrays
        for i in range(1, n - 3 * k + 1):
            # Update the sums of the three subarrays using the sliding window technique
            sum1 = sum1 - nums[i - 1] + nums[i + k - 1]  # Update sum1 for the new window
            sum2 = sum2 - nums[i + k - 1] + nums[i + 2 * k - 1]  # Update sum2 for the new window
            sum3 = sum3 - nums[i + 2 * k - 1] + nums[i + 3 * k - 1]  # Update sum3 for the new window

            # Update the maximum sum for the first subarray if a new maximum is found
            if sum1 > max1:
                max1 = sum1
                index1 = i  # Update the starting index of the first subarray

            # Update the maximum sum for the first two subarrays if a new maximum is found
            if max1 + sum2 > max12:
                max12 = max1 + sum2
                index12_1 = index1  # Update the starting index of the first subarray in the first two
                index12_2 = i + k   # Update the ending index of the second subarray

            # Update the maximum sum for all three subarrays if a new maximum is found
            if max12 + sum3 > max123:
                max123 = max12 + sum3
                ans = [index12_1, index12_2, i + 2 * k]  # Update the best indices

        return ans  # Return the indices of the three subarrays with the maximum sum
        
'''
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
