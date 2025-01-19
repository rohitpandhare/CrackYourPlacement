class Solution(object):
    def trapRainWater(self, heightMap):
      '''
      I'm beginner and taken help of solution for this HARD problem
      '''
        # Edge case: If the heightMap is too small to trap water
        if not heightMap or not heightMap[0] or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = []
        
        # Add all boundary cells to the min-heap
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water_trapped = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Process the heap
        while min_heap:
            height, r, c = heapq.heappop(min_heap)

            # Check all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # Calculate trapped water
                    water_trapped += max(0, height - heightMap[nr][nc])
                    # Push the updated height into the heap
                    heapq.heappush(min_heap, (max(height, heightMap[nr][nc]), nr, nc))

        return water_trapped
