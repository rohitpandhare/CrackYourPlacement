class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort() #sort the array for reducing complexity and more combinations of 2 no. s

        for i, val in enumerate(nums):
            #if the current val is same as prev
            if i > 0 and val == nums[i-1]:
                continue #skip that portion

            left = i +1 #pointer 1- just after current element
            right = len(nums) - 1 #pointer 2- at end 

            while left < right:
                threeSum = val + nums[left] + nums[right] #find the 3sum with current and values at 2 pointers

                if threeSum > 0:
                    right -= 1 #move the right pointer to left (opposite) side
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([val,nums[left],nums[right]]) #appending result
                    #moving the left again
                    left += 1
                    #to resolve the duplicates at END -- to skip any duplicate found
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result #has list of all unique triplets
                
