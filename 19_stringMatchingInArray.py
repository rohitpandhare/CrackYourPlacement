class Solution(object):
    def stringMatching(self, words):
        res = [] #to store the subString results
        for i in range(len(words)):
            for j in range(len(words)):
                #when we are compairing with word itself
                if i ==j: #if its the same word
                    continue
                if words[i] in words[j]: #if the sub string present 
                    res.append(words[i]) #append the substring
                    break
        return res
        
