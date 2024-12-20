class Solution(object):
    def twoSum(self, nums, target):
    #the first loop will act as outer loop
        for i in range(len(nums)):
        #since we are compairing two elements adjacent -- use second loop and start it from 'i+1'
            for j in range(i+1,len(nums)):
              #now we will just compare i & j -- even its iterating
                if (nums[i] + nums[j] == target):
                    return [i,j]
        
