class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return "" #the arrays of strings is empty -- return ""

        prefix = strs[0] #intialize the first string element as prefic

        for string in strs[1:]: #start from the next element 
            while string.find(prefix) != 0:#when prefix is not a prefix of current string
                prefix = prefix[:-1] #remove last char from prefix and check ---  
                if not prefix: #if no common prefix
                    return "" #return ""
        return prefix
