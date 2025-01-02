class Solution(object):
    def maxArea(self, height):
        """ - Brute force--
        max_area = 0
        #i for left, j for right
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                #calculating width
                w = j - i
                h = min(height[i],height[j]) #calculating height
                area = w * h
                max_area = max(area,max_area)
        return max_area
        """
        #using 2 pointer approach
        left = 0
        right = len(height) - 1
        max_area = 0
        #since the left bar decides the height of water -- we take it for case comparisons
        while left < right:
            width = right - left #gap betn bars
            ht = min(height[left],height[right]) #min bar height 
            area = width * ht #calculate are
            max_area = max(max_area,area) #find max area

            if height[left] < height[right]: #if left side is Smallll
                left += 1 #increase pointer
            else: #if left is BIgggg
                right -= 1 #decrease the right pointer
     
        return max_area
  
        
