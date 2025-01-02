class Solution(object):
    def vowelStrings(self, words, queries):
        vowel_set = set("aeiou")
        prefix_cnt = [0] * (len(words) + 1) #making an array full of zeros -- but with one extra space for comparision purpose -- compare with previous
        prev = 0

        for i,w in enumerate(words):
            #check if the first and last alphabet is a vowel by checking 0th and -1th index
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev += 1 #increase vowel count
            #if the index value is a vowel and we made that array of zeros - and will make updated values -- like 0 1 1 2 3 4 5 ...( by adding up + v)
            prefix_cnt[i+1] = prev # store the next element in array by prev value

        result = [0] * len(queries) #make new arrays of zeros 

        for i,q in enumerate(queries):
            l,r = q
            result[i] = prefix_cnt[r + 1] - prefix_cnt[l]
        return result
