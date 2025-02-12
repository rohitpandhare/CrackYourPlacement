class Solution(object):
    def maximumSum(self, nums):
        d = defaultdict(int) #dictionary will store the max number of each digit sum
        res = -1
        for c in nums:
            #calculate the digit sum of the current number
            digit_sum = sum(int(digit) for digit in str(c))

            #If we have seen this digit sum before
            if digit_sum in d:
                res = max(res, d[digit_sum] + c)
            
            #Update the dictionary to store the maximum value for this digit sum
            d[digit_sum] = max(d[digit_sum], c)
        return res
            


        
