class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0          # To store the count of subarrays
        curSum = 0         # This will keep the current cumulative sum
        prefixSum = {0: 1}  # This dictionary keeps track of prefix sums and their counts

        for n in nums:
            curSum += n                  # Update the current cumulative sum
            diff = curSum - k           # Find the difference
            
            result += prefixSum.get(diff, 0)  # Add the count of how many times (curSum - k) has been seen
            
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)  # Record the current cumulative sum in the dictionary

        return result
