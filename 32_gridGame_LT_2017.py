class Solution(object):
    def gridGame(self, grid):
        """
        My understanding: the problem is to --
        make find the min sum of path that robo 2 will follow

        - intially we have 2 robos - 1 & 2
        both will go through the 2 * n ==> 2D matrix
        and thus the robo 1 will be having 'n' oppurtinities for going from top left corner to bottom right corner
        - so ==> the robo 1 's path will be marked as 0's 
        - and robo will get that converted path --
        robo wanted to minimize the path dist.

        but here robo 2 wants to maximize it ==
        simply it will cover that other path than robo 1 ;s path
        -- and thus it will take the sum of 1st array or 2nd array from the 2D matrix
        """
        n = len(grid[0]) #count the number of columns
        if n < 2:
            return 0 # the matrix is too small

        top_sum = sum(grid[0]) #taken the sum of 1st array -- 1st row
        bottom_sum = 0 # a pointer for tracking the paths covered by robo 2
        robo1_req = float('inf') #the min sum is kept to some infinity value

        for p in range(n): #passing through the times of cols
            top_sum -= grid[0][p] #Update score of robo2 == reduce the count of [0][that one element from the path is changed]
            # Robot2's possible scores based on Robot1's current path
            robo2_req = max(top_sum, bottom_sum)
            
            # Minimize the score that Robot1 can ensure
            robo1_req = min(robo1_req, robo2_req)

            # Update the bottom_sum with the current position in the second row
            bottom_sum += grid[1][p]

        return robo1_req  # Return the minimized score for Robot1
