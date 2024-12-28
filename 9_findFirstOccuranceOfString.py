class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Handle the case of an empty needle
        if not needle:
            return 0
        
        # Get the length of needle to use for slicing
        e = len(needle)
        
        # Loop through the haystack
        for i in range(len(haystack) - e + 1):
            # Check if the current slice matches the needle (from i-th element to i + len(needle) )
            if haystack[i:i+e] == needle:
                return i
        
        # else
        return -1
'''
# By using inbuilt functions --
if needle not in haystack:
            return-1
        else:
            return haystack.find(needle)
'''
