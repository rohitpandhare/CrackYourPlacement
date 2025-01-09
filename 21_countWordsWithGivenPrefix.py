class Solution(object):
    def prefixCount(self, words, pref):
        count = 0 #start the counter with
        for i in range(len(words)): ##loop through the words
            if words[i].startswith(pref): #check if words[i] starts with pref
                count += 1 #increase counter
        return count #return counter
        
        
