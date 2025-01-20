class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        rows, cols  = len(mat),len(mat[0]) #count the rows and columns (m*n)

        mat_to_position = {} #created a hash map to save the position of element (r,c)
        for r in range(rows):
            for c in range(cols):
                mat_to_position[mat[r][c]] = (r,c)
        
        row_count = [0] * rows #created an 0's array equal to rows size
        col_count = [0] * cols #did same for cols

        for i in range(len(arr)):
            r,c = mat_to_position[arr[i]] #fetch the coordinates -- to row and cols again
            #if its present in array - color it ==> increase row or cols count
            row_count[r] += 1
            col_count[c] += 1

            if col_count[c] == rows or row_count[r] == cols: #check if any - row or col is completely filled
                return i #return the index of the element in array that satifies the condition
