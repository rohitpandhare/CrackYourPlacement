class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
        island_sizes = {0: 0}  # Store island sizes, default 0 for water
        island_id = 2  # Start from 2 to differentiate from original 1s
        
        # s. 1: Find all islands and mark them with unique IDs
        def dfs(r, c, id):
            # DFS to calculate island size and mark all its cells with ID.
            stack = [(r, c)]
            grid[r][c] = id
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id
                        stack.append((nx, ny))
            return size

        # Identify islands and assign unique IDs
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # s. 2: Try flipping each 0 and calculate the max possible island size
        max_island = max(island_sizes.values())  # Get the max existing island size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_ids = set()
                    new_size = 1  # We flip this 0 to 1
                    for dx, dy in directions:
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            island_id = grid[nx][ny]
                            if island_id not in seen_ids:
                                seen_ids.add(island_id)
                                new_size += island_sizes[island_id]

                    max_island = max(max_island, new_size)  # Update the largest island size

        return max_island
