class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(arr,start,end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start] #swapping it
                start += 1
                end -= 1

        #Reverser the entire array
        reverse(nums,0,n-1)

        #reverse the first k elements
        reverse(nums,0,k-1)

        #reverse the rest of array
        reverse(nums,k,n-1)
