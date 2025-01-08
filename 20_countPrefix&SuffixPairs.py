class Solution(object):
    def countPrefixSuffixPairs(self, words):
        res = 0 #intialize a variable

        for i in range(len(words)): #loop 1
            for j in range(i+1,len(words)): #loop2

                w1,w2 = words[i],words[j] #store the past and next word in w1 and w2
                n = len(w1) #store the length of first array

                # if w1 == w2[:n] and w1 == w2[-n:]: #method 1-- check if the i-th word == j-th word(start-->end) and i-th word === j-th words(reverse to mid)
                if w2.startswith(w1) and w2.endswith(w1): #method 2
                    res += 1 #store result
        return res #print
        
