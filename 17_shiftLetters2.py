class Solution(object):
    def shiftingLetters(self, s, shifts):
        prefix_diff = [0] * (len(s)+1) #create an array of zeros +1 for smooth operations

        #for left and right part in array of input
        for left, right, val in shifts:
            #short if else 
          # 0 for backward shift (-1) -- 1 for forward shift (+1)
            prefix_diff[right+1] += 1 if val else -1
            prefix_diff[left] += -1 if val else 1

        diff = 0 #a temporary variable
        result = [ord(char) - ord("a") for char in s] #use list comprehension to store all the values in number form by making -AsCII of a  eg. if char is 'b' make it 98'[b] - 97(a) = 1

        for i in reversed(range(len(prefix_diff))): #parse through array where prefix diff stored
            diff += prefix_diff[i] #simply copying value at current in diff
            result[i-1] = (diff + result[i-1]) %26

        s = [chr(ord("a") + ele) for ele in result]
        return "".join(s)
