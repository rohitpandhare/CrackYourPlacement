from collections import deque

class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        # Initialize a list to hold groups of numbers. Each group will be a queue (deque).
        groups = []  # Creating a list of queues

        # Initialize a dictionary to map each number to its corresponding group index.
        num_to_group = {}  # nums[i] -> group index

        # Sort the numbers to process them in ascending order.
        for n in sorted(nums):
            # If no groups exist or the current number 'n' cannot be added to the last group
            # without exceeding the 'limit', create a new group.
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())  # Append a new empty deque to groups

            # Add the current number 'n' to the last group.
            groups[-1].append(n)

            # Map the current number 'n' to its group index.
            num_to_group[n] = len(groups) - 1

        # Initialize the result list to build the final lexicographically smallest array.
        res = []

        # Iterate through the original 'nums' array to maintain the original order.
        for n in nums:
            # Retrieve the group index for the current number 'n'.
            j = num_to_group[n]

            # Pop the leftmost element from the corresponding group and append it to the result.
            res.append(groups[j].popleft())

        # Return the constructed lexicographically smallest array.
        return res
