class Solution(object):
    def majorityElement(self, nums):
      #let's take the first number in array as majority for an instance
        maj = nums[0]
      #make a counter to count the occurances
        count = 1

      #since we kept maj as nums[0]  ,, loop should check from next element
        for i in range(1,len(nums)):
            if count == 0: #check if the counter is 0, make it 1-- becoz a element is present at least once
                maj = nums[i] #make current element as maj 
                count = 1 # updating counter
            
            elif maj == nums[i]: #when the same number occurs multiple times
                count += 1 #counter updated as per the occurances
            else:
                count -= 1 # when numbers do not match -- simple decrease counter-- sometimes it may reach to 0
        return maj


#non-optimal solution-
'''
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums) #store length

        for i in range((n//2) + 1): #checl from0 to half part in array
            count = 0 #keep counter as 0
            
            for j in range(i,n): #inner loop for checking all elements
                if nums[i] == nums[j]: #if we found the half elements array is matching some other element
                    count +=1 #counter is increased
                    
                    if count > n //2: #if the majority elements has count > floor div(nums length) --half array
                        return nums[i] #return the majority element
        return 0 #else part 
      '''
