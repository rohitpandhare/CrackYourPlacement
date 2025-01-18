class Solution(object):
    def minCost(self, grid):
        """
        #taken help
        Approach
        1)Use a 0-1 BFS (Breadth-First Search) algorithm with a deque (double-ended queue).
        2)Initialize a 2D array minCost to store the minimum cost to reach each cell.
        3)Start from the top-left cell (0,0) and explore neighboring cells.
        4)If the current direction matches the grid's direction, add the cell to the front of the deque (no cost).
        5)If the direction doesn't match, add the cell to the back of the deque (cost of 1).
        6)Continue until the bottom-right cell is reached or all cells are explored.
        Complexity
        """
        m, n = len(grid), len(grid[0])
        # Initialize the minCost matrix with a large value
        minCost = [[float('inf')] * n for _ in range(m)]
        minCost[0][0] = 0
        
        # Deque for 0-1 BFS
        dque = deque([(0, 0)])
        
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while dque:
            r, c = dque.popleft()
            
            # Visit adjacent cells
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0
                
                if 0 <= nr < m and 0 <= nc < n and minCost[r][c] + cost < minCost[nr][nc]:
                    minCost[nr][nc] = minCost[r][c] + cost
                    
                    # Add to deque based on cost
                    if cost == 1:
                        dque.append((nr, nc))
                    else:
                        dque.appendleft((nr, nc))
        
        # Return the minimum cost to reach the bottom-right corner
        return minCost[m - 1][n - 1]
