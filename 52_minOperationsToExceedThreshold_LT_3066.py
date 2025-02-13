class Solution(object):
    def minOperations(self, nums, k):
        #create a min-heap using heapq
        minheap = []

        for n in nums:
            heapq.heappush(minheap,n) #add all elements tp heap

        count = 0 #counter for the no. of operations
        while minheap:
            min1 = heapq.heappop(minheap) #get the first smallest element in minheap
            if min1 >= k:
                break #break this elements
            min2 = heapq.heappop(minheap) #get second smallest element\

            #pushing the calculted element in heap
            heapq.heappush(minheap, 2 *(min(min1,min2)) + (max(min1,min2)))
            count += 1
        return count


        
