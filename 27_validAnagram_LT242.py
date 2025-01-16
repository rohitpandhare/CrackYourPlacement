class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False #return false when length are not same
        
        freq = [0] * 26 #create array of all alphabets

        for i in range(len(s)): #for loop
            freq[ord(s[i]) - ord('a')] += 1 #append freq when occured in S
            freq[ord(t[i]) - ord('a')] -= 1 #pop freq when occured in T
        
        for i in range(len(freq)): #for loop in freq
            if freq[i] != 0: #return true on freq = 0--- now here we just return False
                return False
                
        return True #Else return True

        
