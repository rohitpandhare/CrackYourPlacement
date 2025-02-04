class Solution:
    def maxAscendingSum(self, nums):
        # Handle empty array case
        if not nums:
            return 0
        
        # Initialize both max_sum and current_sum with first element
        # current_sum tracks current ascending subarray sum
        # max_sum tracks largest ascending subarray sum found so far
        max_sum = current_sum = nums[0]
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # If current number is greater than previous number
            # Add it to current ascending subarray sum
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            # If current number is less than or equal to previous
            # Start new ascending subarray from current number
            else:
                current_sum = nums[i]
            
            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)
        
        # Return the largest ascending subarray sum found
        return max_sum
