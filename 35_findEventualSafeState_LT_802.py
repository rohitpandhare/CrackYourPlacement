class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        WHITE, GRAY, BLACK = 0, 1, 2  # Node states: unvisited, visiting, safe
        color = [WHITE] * n  # Initialize all nodes as unvisited

        def is_safe(node):
            if color[node] != WHITE:
                return color[node] == BLACK  # Return True if already marked safe

            color[node] = GRAY  # Mark the node as visiting
            for neighbor in graph[node]:
                if color[neighbor] == GRAY or not is_safe(neighbor):
                    return False  # Found a cycle or an unsafe path

            color[node] = BLACK  # Mark the node as safe
            return True

        # Collect all safe nodes
        safe_nodes = [node for node in range(n) if is_safe(node)]
        return safe_nodes
