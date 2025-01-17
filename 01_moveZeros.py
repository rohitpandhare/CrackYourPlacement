class Solution(object):
    def moveZeroes(self, nums):
        #create a variable which will track 
        pos = 0
        for i in range(len(nums)):
          #when the elements in array are non-zero
            if nums[i] != 0:
              # copy the current element to the pos 
                # the current VALUE is updated the POS position
                nums[pos] = nums[i]
              #update the pos -- so that will be used in next for loop for iteration and zero addition
                pos +=1

        # start from end of non-zero element (POS) to end of nums array
        for i in range(pos,len(nums)):
          #only append required zeros
            nums[i] = 0
        return nums
        
