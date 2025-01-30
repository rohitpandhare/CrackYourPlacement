from collections import deque

class Solution:
    def isComponentBipartite(self, adj, state, start):
        q = deque([start])
        state[start] = 1
        
        # Apply BFS
        while q:
            curr = q.popleft()
            for nbr in adj[curr]:
                if state[nbr] == 0:
                    state[nbr] = -1 * state[curr]
                    q.append(nbr)
                elif state[nbr] == state[curr]:
                    return False
        return True
    
    def checkBipartiteGraph(self, adj, n):
        state = [0] * (n + 1)
        for i in range(1, n + 1):
            if state[i] == 0 and not self.isComponentBipartite(adj, state, i):
                return False
        return True
    
    def countLevels(self, adj, n, source):
        visited = [False] * (n + 1)
        q = deque([source])
        visited[source] = True
        levels = 0
        
        # Apply BFS
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for nbr in adj[curr]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        q.append(nbr)
            levels += 1
        return levels
    
    def findMaxLevelsBFS(self, max_distance, adj, visited, source):
        q = deque([source])
        visited[source] = True
        max_levels = -1
        
        # Apply BFS
        while q:
            curr = q.popleft()
            max_levels = max(max_levels, max_distance[curr])
            for nbr in adj[curr]:
                if not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)
        return max_levels
    
    def magnificentSets(self, n, edges):
        # Step-1: Make adjacency List
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        # Step-2: Check if the graph is Bipartite
        if not self.checkBipartiteGraph(adj, n):
            return -1
        
        # Step-3: Calculate Max Distance from each node (using BFS)
        max_distance = [0] * (n + 1)
        for i in range(1, n + 1):
            max_distance[i] = self.countLevels(adj, n, i)
        
        # Step-4: Find the max distance count per component
        visited = [False] * (n + 1)
        total_levels = 0
        for i in range(1, n + 1):
            if not visited[i]:
                total_levels += self.findMaxLevelsBFS(max_distance, adj, visited, i)
        
        return total_levels
