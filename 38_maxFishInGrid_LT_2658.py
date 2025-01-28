class Solution:
    
    def __init__(self):
        # Initialize direction vectors for navigating up, right, down, and left
        # The 'dir' list holds [dx1, dy1, dx2, dy2, dx3]
        # This allows us to access (dx, dy) pairs using indices
        self.dir = [-1, 0, 1, 0, -1]
    
    def is_valid(self, x, y, m, n):
        """
        Check if the (x, y) coordinates are within the bounds of the grid.
        
        Parameters:
        - x (int): Current row index
        - y (int): Current column index
        - m (int): Total number of rows in the grid
        - n (int): Total number of columns in the grid
        
        Returns:
        - bool: True if (x, y) is within bounds, False otherwise
        """
        return 0 <= x < m and 0 <= y < n
    
    def dfs(self, grid, visited, m, n, x, y):
        """
        Perform Depth-First Search (DFS) to explore all connected cells with fish.
        
        Parameters:
        - grid (List[List[int]]): 2D grid representing the number of fish in each cell
        - visited (List[List[bool]]): 2D grid to track visited cells
        - m (int): Total number of rows
        - n (int): Total number of columns
        - x (int): Current row index
        - y (int): Current column index
        
        Returns:
        - int: Total number of fish in the connected region
        """
        # Start with the fish count in the current cell
        fish_count = grid[x][y]
        
        # Explore all four directions: up, right, down, left
        for i in range(4):
            # Calculate new coordinates based on direction vectors
            new_x = x + self.dir[i]
            new_y = y + self.dir[i + 1]
            
            # Check if the new cell is valid, not visited, and contains fish
            if self.is_valid(new_x, new_y, m, n) and not visited[new_x][new_y] and grid[new_x][new_y] > 0:
                # Mark the new cell as visited
                visited[new_x][new_y] = True
                # Recursively explore the new cell and add its fish to the total count
                fish_count += self.dfs(grid, visited, m, n, new_x, new_y)
        
        return fish_count
    
    def findMaxFish(self, grid):
        """
        Find the maximum number of fish in any connected region of the grid.
        
        Parameters:
        - grid (List[List[int]]) : 2D grid representing the number of fish in each cell
        
        Returns:
        - int: Maximum number of fish found in a single connected region
        """
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        # Initialize the maximum fish count to zero
        max_fish = 0
        # Create a visited grid initialized to False
        visited = [[False] * n for _ in range(m)]
        
        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the cell has not been visited and contains fish
                if not visited[i][j] and grid[i][j] > 0:
                    # Mark the cell as visited
                    visited[i][j] = True
                    # Perform DFS to find the total fish in this connected region
                    current_fish = self.dfs(grid, visited, m, n, i, j)
                    # Update the maximum fish count if current region has more fish
                    max_fish = max(max_fish, current_fish)
        
        return max_fish
