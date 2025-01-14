class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        freq = [0] * (n+1) #0th location is dummy location --0
        res = [0] * n #result array of exact same size
        count = 0 #counter

        for i in range(n): #use single for loop for ease
            freq[A[i]] += 1 #if any element occur update its counter
            if freq[A[i]] == 2:
                count += 1 # increase the counter when that element is found twice --from both A & B
            freq[B[i]] += 1 #increment freq counter for the elements in B also
            if freq[B[i]] == 2:
                count += 1 # increase the counter when that element is found twice --from both A & B

            res[i] = count
        return res
