class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2: #if the strings are equal return true
            return True
        n = len(s1) #store length
        mismatches = 0 #intialize a variable
        mismatch = [] #array here
        pos = 0

        while pos < n: #check under req length 
            if s1[pos] != s2[pos]: #when the position of both are diff,,,
                mismatch.append(s1[pos]) #append mismatch
                mismatch.append(s2[pos])
                mismatches += 1 #append counts
            pos += 1
        if len(mismatch) == 4:
            return mismatch[0] == mismatch[3] and mismatch[1] == mismatch[2] #if ABBA -- the A and A are same and same with B
        return False #else return false
        


        



        
        
