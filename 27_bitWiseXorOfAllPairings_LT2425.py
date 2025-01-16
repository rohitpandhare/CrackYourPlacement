class Solution(object):
    def xorAllNums(self, nums1, nums2):
        '''
        #BruteForce
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                res ^= n1 ^ n2
        return res
        '''
        res = 0
        #since the even terms like 1010 ^ 1010 is even --then it will cancel - so it will cancel it out
        if len(nums1) % 2 == 1:    # If nums1 length is odd
            for n in nums2:        # Each number in nums2 will appear odd times
                res ^= n          # So we XOR all nums2 elements
        
        if len(nums2) % 2 == 1:    # If nums2 length is odd
            for n in nums1:        # Each number in nums1 will appear odd times
                res ^= n          # So we XOR all nums1 elements

        return res

        
