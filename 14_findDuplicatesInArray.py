class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort() #sort array
        dup = [] #make an empty array

        if len(nums) < 2: # when len is less than 2 -- here min length is 1 not 0 
            return dup #return empty dup []

        for i in range(1,len(nums)): #to avoid conflicts, start the loop with index 1, (basucakky we have index from 0)
                if nums[i-1] == nums[i]: #check nearby element
                    dup.append(nums[i]) #append the dupicate array 
        return dup #return duplicate array
                
        
