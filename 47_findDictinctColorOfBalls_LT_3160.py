class Solution(object):
    def queryResults(self, limit, queries):
        # Initialize the result list to store the number of distinct colors after each query
        res = []  # res[i] = distinct number of colors after queries[i]
        
        # Variable to track the current count of distinct colors
        distinct = 0 

        # Dictionary to map each ball to its currently assigned color
        ball_color = {}  

        # Dictionary to track the count of each color
        # {color: number of balls with this color}
        color_count = {}  

        # Iterate over each query in the list of queries
        for ball, new_color in queries:
            # Step 1: Handle the removal of the ball's previous color assignment (if it exists)
            if ball in ball_color:
                # Retrieve the old color of the current ball
                old_color = ball_color[ball]
                
                # Decrement the count for the old color
                color_count[old_color] -= 1
                
                # If the count of the old color becomes zero, it means this color is no longer used
                if color_count[old_color] == 0:
                    # Remove the old color from the color count dictionary
                    del color_count[old_color]
                    
                    # Reduce the total count of distinct colors
                    distinct -= 1

            # Step 2: Assign the new color to the ball and update the color count
            # Update the ball's color in the `ball_color` dictionary
            ball_color[ball] = new_color
            
            # If the new color is already being used, increment its count
            if new_color in color_count:
                color_count[new_color] += 1
            else:
                # If the new color is not being used, add it to `color_count` with an initial count of 1
                # This also means a new distinct color is now present
                color_count[new_color] = 1
                distinct += 1

            # Step 3: Append the current total number of distinct colors to the result list
            res.append(distinct)
        
        # After processing all the queries, return the result list
        return res
