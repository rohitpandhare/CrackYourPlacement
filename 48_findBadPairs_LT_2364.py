class Solution(object):
    def countBadPairs(self, nums):
        n = len(nums)

        #total number of pairs
        total_pair = n * (n - 1) //2

        #Dictionary to count the frequency of (nums[i] - i)
        freq = {}
        good_pairs = 0


        for i in range(n):
            diff = nums[i] - i

            if diff in freq:
                good_pairs += freq[diff]
            freq[diff] = freq.get(diff,0) + 1

        #total bad pairs is complement of good pairs
        return total_pair - good_pairs
