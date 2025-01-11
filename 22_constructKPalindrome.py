class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k > len(s): #if the target is small result False
            return False
        
        count = Counter(s) #store the count of each letter here
        odd = 0 #intialize a variable

        for c in count.values(): #checking values
            odd = odd + c %2 #if the count of letter is odd - increment by 1
        return odd <= k #return True if the odds are less than or equal to k

        
