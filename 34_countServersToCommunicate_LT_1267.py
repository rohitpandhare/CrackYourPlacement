class Solution(object):
    
    def countServers(self, grid):
    
        total_servers = 0
    
        row_cnt = [0] * len(grid)  # rows
    
        col_cnt = [0] * len(grid[0])  # cols
    
        # First pass: Count the number of servers in each row and column
        for i in range(len(row_cnt)):
            for j in range(len(col_cnt)):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
    
        # Second pass: Count servers that can communicate (s > 1)
        for i in range(len(row_cnt)):
            for j in range(len(col_cnt)):
                if grid[i][j] == 1 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    total_servers += 1
    
        return total_servers
