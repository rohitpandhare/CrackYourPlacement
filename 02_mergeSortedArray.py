class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #start for loop with length of second array-- 
        for i in range(n):
            #and then insert ---m-- + with nums2 elements
            nums1[m+i] = nums2[i]
        #simple sort 
        nums1.sort()

