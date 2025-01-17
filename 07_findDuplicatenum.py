class Solution(object):
    def findDuplicate(self, nums):
    
        seen = set()  # To track we got
        for num in nums:
            if num in seen:  # If the number is already in the set, it's the duplicate
                return num
            seen.add(num)  # Otherwise, add the number to the set
