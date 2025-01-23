class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)): #count how many times the val is present
                nums.remove(val) #remove the val occurance at that time
                
        
