from collections import deque  # Import deque from collections for efficient FIFO queue operations

class Solution(object):
    def isValid(self, x, y, m, n):
        """
        Helper method to check if the given coordinates are within the grid bounds.
        
        :param x: Current row index
        :param y: Current column index
        :param m: Total number of rows in the grid
        :param n: Total number of columns in the grid
        :return: True if (x, y) is within bounds, False otherwise
        """
        return 0 <= x < m and 0 <= y < n  # Return True if x and y are within the grid, else False

    def highestPeak(self, isWater):
        """
        Assigns heights to each cell in the grid based on their distance from the nearest water cell.
        Water cells are assigned height 0, and each land cell's height is 1 plus the minimum height of its adjacent cells.
        
        :type isWater: List[List[int]]  # 2D grid where 1 represents water and 0 represents land
        :rtype: List[List[int]]         # 2D grid with heights assigned to each cell
        """
        m, n = len(isWater), len(isWater[0])  # Determine the number of rows (m) and columns (n) in the grid
        
        # Initialize the height grid with -1 for all cells to indicate unprocessed land cells
        height = [[-1] * n for _ in range(m)]  
        
        queue = deque()  # Initialize a deque to use as a queue for BFS
        
        # Iterate over each cell in the grid to find water cells and initialize them in the queue
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:  # Check if the current cell is a water cell
                    queue.append((i, j))  # Add water cell coordinates to the queue as starting points for BFS
                    height[i][j] = 0      # Set the height of water cells to 0
        
        # Define the four possible directions to move: up, right, down, and left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Perform BFS starting from all water cells simultaneously
        while queue:
            x, y = queue.popleft()          # Dequeue the next cell (x, y) to process
            current_height = height[x][y]   # Get the current height of the dequeued cell
            
            # Explore all four adjacent directions
            for dx, dy in directions:
                newX, newY = x + dx, y + dy  # Calculate the coordinates of the adjacent cell
                
                # Check if the adjacent cell is within bounds and has not been assigned a height yet
                if self.isValid(newX, newY, m, n) and height[newX][newY] == -1:
                    height[newX][newY] = current_height + 1  # Assign height as one more than current cell's height
                    queue.append((newX, newY))               # Enqueue the adjacent cell for further processing
        
        return height  # Return the completed height grid
