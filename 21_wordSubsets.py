class Solution(object):
    def wordSubsets(self, words1, words2):
        req = Counter() #intialize a counter to track words
        for word in words2: #to check the words in w2
            cur = Counter(word) #iterate by a counter
            for ch in cur: #for loop to store the max iterations 
                req[ch] = max(req[ch], cur[ch]) #compare the current with max counter
        
        ans = [] #to check ans
        for word in words1: 
            cur = Counter(word) #here we used counter to store the matched words in ans list
            if all(cur[ch] >= req[ch] for ch in req): #if the words2 really present in words1
                ans.append(word) #append word
        
        return ans #show result
        ''' Failed Solution -- but has good LOGIC
        res = set()        
        for i in range(len(words1)):
            for j in range(len(words2)):

                if (words2[j] in words1[i]) and (words1[j+1] in words1[i]):
                    res.add(words1[i])
        return list(res)'''
   
