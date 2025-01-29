class Solution(object):
    # Find function implements path compression in disjoint set
    def find(self, disVal, v):
        # If the value at index v is -1, it means this node is a root/parent
        # or it's a standalone node
        if disVal[v] == -1:
            return v
        
        # Recursively find the parent and compress the path
        # by making all nodes in path point directly to root
        disVal[v] = self.find(disVal, disVal[v])
        return disVal[v]

    def findRedundantConnection(self, edges):
        """
        Purpose: Find an edge that can be removed to convert a graph into a tree
        Input: List of edges where each edge is [node1, node2]
        Output: The last edge that creates a cycle
        """
        # n is number of edges
        n = len(edges)
        
        # Initialize disjoint set array with -1
        # Size is n+1 because nodes are 1-indexed
        disVal = [-1] * (n+1)
        
        # Process each edge
        for edge in edges:
            # Find parents of both nodes in the edge
            parent_x = self.find(disVal, edge[0])
            parent_y = self.find(disVal, edge[1])

            # If both nodes have same parent, we found a cycle
            # This edge is redundant and can be removed
            if parent_x == parent_y:
                return edge
            else:
                # Union operation: Make parent_y the parent of parent_x
                disVal[parent_x] = parent_y

        # Return [0,0] if no redundant edge found (shouldn't happen given constraints)
        return [0,0]
