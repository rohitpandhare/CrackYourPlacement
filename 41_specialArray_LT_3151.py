class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1: #if the length is 1 -- its uniquw
            return True
        else:
            for i in range(1,len(nums)): #start from 1 and next
                if (nums[i] & 1) == (nums[i-1] & 1): #check if the both adjacent even or odd there
                    return False #return false
            return True #else True
