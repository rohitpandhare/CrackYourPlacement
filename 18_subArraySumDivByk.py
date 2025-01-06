class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        count = 0
        for i in range(len(nums)):
            sum_subarray = 0
            for j in range(i,len(nums)):
                sum_subarray += nums[j]
                if sum_subarray % k == 0:
                    count += 1
        return count """
        # Initialize prefix sum array
        prefix_sum = {0: 1}  # Key: remainder, Value: frequency
        curr_sum = 0
        count = 0

        for n in nums: #go through each sub array
            curr_sum += n #save the current sum
            remainder = curr_sum % k #check if its div by k or not
            
            if remainder in prefix_sum: #if remainder exists in prefix_sum update it
                count += prefix_sum[remainder] #increase count
            
            # Update the frequency of current remainder
            prefix_sum[remainder] = prefix_sum.get(remainder, 0) + 1 #if we get that reamainder -- update its frequncy
        
        return count #of remainder 0 


                   
