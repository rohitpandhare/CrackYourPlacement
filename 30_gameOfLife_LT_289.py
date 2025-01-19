class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Helper function to check if a neighbor position is within board boundaries
        def isValidNeighbor(x, y, board):
            return (x >= 0 and x < len(board) and y >= 0 and y < len(board[0]))
        
        # Define direction arrays for all 8 possible neighbors
        # dx and dy together form coordinate pairs: (0,1), (0,-1), (1,1), etc.
        dx = [0, 0, 1, 1, 1, -1, -1, -1]  # Changes in x direction
        dy = [1, -1, 1, -1, 0, 0, 1, -1]  # Changes in y direction
        
        # Iterate through each cell in the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Counter for live neighbors of current cell
                count_live_neighbors = 0
                
                # Check all 8 neighbors of current cell
                for i in range(8):
                    # Calculate neighbor coordinates
                    curr_x = row + dx[i]
                    curr_y = col + dy[i]
                    # If neighbor is valid and is/was alive (1 or -1), increment counter
                    if isValidNeighbor(curr_x, curr_y, board) and abs(board[curr_x][curr_y]) == 1:
                        count_live_neighbors += 1
                
                # Rule 1 & 3: Live cell dies if it has < 2 or > 3 live neighbors
                # Mark as -1 (was alive, now dead)
                if board[row][col] == 1 and (count_live_neighbors < 2 or count_live_neighbors > 3):
                    board[row][col] = -1
                
                # Rule 4: Dead cell becomes alive if it has exactly 3 live neighbors
                # Mark as 2 (was dead, now alive)
                if board[row][col] == 0 and count_live_neighbors == 3:
                    board[row][col] = 2
        
        # Final pass to update board
        # Convert all interim states to their final states
        for row in range(len(board)):
            for col in range(len(board[0])):
                # If cell is >= 1 (1 or 2), it's alive in next state
                if board[row][col] >= 1:
                    board[row][col] = 1
                # If cell is < 1 (0 or -1), it's dead in next state
                else:
                    board[row][col] = 0
