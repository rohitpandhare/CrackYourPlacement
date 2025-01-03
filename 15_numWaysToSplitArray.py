class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we are making 2 splits 
        # the sum side --splitted---| ----sum---
        sums = sum(nums) #right sum pointer sum
        left = 0 #left pointer sum
        count = 0 #result

        for i in range(len(nums) - 1): #ranging len -1
            left += nums[i] #increase left pointer
            sums -= nums[i] #increase sums pointer

            if left >= sums: #if the left is big than sum
                count += 1 #increase count
        return count #return count
        
