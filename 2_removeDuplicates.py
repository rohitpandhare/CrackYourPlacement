class Solution(object):
    def removeDuplicates(self, nums):
      #for iterating
        i = 0  

        for j in range(len(nums)): 
          #this will check if the current element is less than the prev elements
            if nums[j] != nums[i]: 
                i += 1  #Moving to next
                nums[i] = nums[j]  #Updating list with unique elments

        return i + 1  # Return unique element length
