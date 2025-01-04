class Solution(object):
    def countPalindromicSubsequence(self, s):
        '''
        r = len(s)
        palindrome = set()

        for i in range(r-2):
            for j in range(i+1,r-1):
                for k in range(j+1,r):
                    if s[i] == s[k]:
                        palindrome.add((s[i],s[j],s[k]))
        return len(palindrome) '''
        #optimal approach

        #created 2 dictionaries to store first and last occurance
        first = {}
        last = {}

        for i,char in enumerate(s): #loop to acces the INdex and Char at index
            if char not in first: #if char is not present in first 
                first[char] = i #add it
            last[char] = i# if the char is IN FIRST -- add that in last
        
        result = 0 #result variable
        for char in first: #checking the first Dictionary
            if first[char] < last[char]: #if the irst char is less occur than last chat -- means there is enough space for Last char to be the same --> palindrome
                ans = s[first[char]+ 1:last[char]] #store all chars betn 1st and last occurance  ==> +1 to skip to the first element : last ==> to not include last char
                unique_char = len(set(ans))# convert that into set _to Eliminate duplicates
                result += unique_char #append that count to result

        return result #willl return number of palindromes
