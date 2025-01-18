class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Create a dictionary to map each element in nums1 to its index
        nums1Idx = {n: i for i, n in enumerate(nums1)}

        # Initialize the result list with -1 for each element in nums1
        res = [-1] * len(nums1)

        # Initialize an empty stack to keep track of elements
        stack = []

        # Iterate through each element in nums2
        for i in range(len(nums2)):
            cur = nums2[i]

            # While the stack is not empty and the current element is greater than the top of the stack
            while stack and cur > stack[-1]:
                # Pop the top element from the stack
                val = stack.pop()

                # Get the index of the popped element in nums1
                idx = nums1Idx[val]

                # Update the result list with the current element
                res[idx] = cur

            # If the current element is in nums1, push it onto the stack
            if cur in nums1Idx:
                stack.append(cur)

        # Return the result list
        return res
