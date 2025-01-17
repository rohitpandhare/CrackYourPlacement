class Solution(object):
    def containsDuplicate(self, nums):
        sums = Counter(nums) #count the iteration of each element in array

        for val in sums.values(): #loop through the values
            if val > 1: #if the value is repeated -- return True
                return True
        return False
        
