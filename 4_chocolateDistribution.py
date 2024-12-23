class Solution:

    def findMinDiff(self, arr,M):

        # code here
        #sort a big array 
        arr.sort()
        #take an infinity value -- to compare
        main_diff = float('inf')

        # start the loop from 0 to len(array) - M(given) +1 --(it's like if an array is of len-10 and m=5 -- so the loop will run from(10-5+1) =4-- from 0 to 4
        for i in range(len(arr)- M +1):
            # find the diff betn  2 position window-- and keep changing the window
            diff = arr[i + M -1] - arr[i]
            #update the new difference -- so that we will get real min
            if diff < main_diff:
                main_diff = diff
        #return main_diff--
        return main_diff
