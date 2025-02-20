class Solution(object):
    def __init__(self):
        self.res = "" #declared empty string
    
    def buildNumber(self,numbers,curr,n):
        if len(curr) == n:
            if curr not in numbers:
                self.res = curr #if current is Unique - Return True
                return True
            return False #else return false
        
        #try '0'
        if self.buildNumber(numbers,curr + '0',n):
         return True
        
        #try '1'
        if self.buildNumber(numbers,curr + '1',n):
            return True
        return False
            
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        numbers = set(nums)
        self.buildNumber(numbers,"",n)
        return self.res
