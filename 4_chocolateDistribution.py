class Solution:

    def findMinDiff(self, arr,M):

        # code here
        arr.sort()
        main_diff = float('inf')
        
        for i in range(len(arr)- M +1):
            diff = arr[i + M -1] - arr[i]
            if diff < main_diff:
                main_diff = diff
        return main_diff
