class Solution(object):
    def smallestNumber(self, pattern):
      #so the pattern has D and I's in it
        res, stack = [],[] #createing 2 array ds - one will act as a stack here

        for s in range(len(pattern) + 1): #looping through this pattern
            stack.append(s + 1) #append any element we found in pattern

            while stack and (s == len(pattern) or pattern[s] == "I"): #Run this while ONly while the stack is not empty --and -- the iterator= len of pattern --or -- the element is 'I'
                res.append(str(stack.pop())) #convert the popped element in string and then append in the result array

        return "".join(res) #join all updated Result part together
        
