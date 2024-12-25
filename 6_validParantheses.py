class Solution(object):
    def isValid(self, s):
        # Mappping the closing bracket with opning
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Initializing an empty stack 
        stack = []
        
        # Iterate over each element
        for element in s:
            # Check if the character is a closing bracket
            if element in bracket_map:
                # Pop the top element from the stack if it's not empty--- else use '#' as a placeholder
                top_element = stack.pop() if stack else '#' #storing the top of stack
                
                # Check if the popped bracket with char map's value part ( key - end brack & val - opening part)
                if bracket_map[element] != top_element:
                    return False  # Return False if mismatch
            else:
                # If it's an opening bracket then push into stack
                stack.append(element)
        
        # at the end the stack will become empty
        return not stack  # Return True if the stack is empty -- stack -empty- false--> not stack -- true !!
