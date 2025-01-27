from collections import defaultdict

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        # Create an adjacency list to represent the graph.
        # Each course points to its list of prerequisites.
        adj = defaultdict(list)

        # Populate the adjacency list with the given prerequisites.
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)  # Append the prerequisite course to the current course's list

        # Initialize a dictionary to map each course to its set of prerequisites
        prereqMap = defaultdict(set)  # Changed from {} to defaultdict(set)

        # Define a helper function to perform Depth-First Search (DFS) to find all prerequisites for a course.
        def dfs(crs):
            # If the course hasn't been processed yet, compute its prerequisites.
            if crs not in prereqMap:
                # Iterate through each prerequisite of the current course
                for prereq in adj[crs]:
                    # Union the prerequisites of the current prerequisite into the current course's prerequisites
                    prereqMap[crs] |= dfs(prereq)
                # A course is always a prerequisite of itself
                prereqMap[crs].add(crs)
            # Return the set of all prerequisites for the current course
            return prereqMap[crs]

        # Perform DFS for each course to populate the prereqMap
        for crs in range(numCourses):
            dfs(crs)

        # Initialize a list to store the results for each query
        res = []

        # Iterate through each query to determine if a course is a prerequisite of another
        for u, v in queries:
            # Check if course u is in the set of prerequisites for course v
            res.append(u in prereqMap[v])

        # Return the list of results corresponding to the queries
        return res
