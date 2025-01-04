class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) #of whole matrix [ number of rowsss] [] [] [] => 3 rows
        n =len(matrix[0]) #of the first row only [ number of column]   - -  - => 3 cols
        zero_pos = []

        for i in range(m): #go through the matrix
            for j in range(n): #go through the top row
                if matrix[i][j] ==0: #if we found the element as 0
                    zero_pos.append([i,j]) #append there index

        for row,col in zero_pos: #pass by row and col in - matrix where the index are stores
                #since n was for - col --> we use row, to make a matix
            for j in range(n): #set row to zero
                matrix[row][j] = 0
                
                #since m was - row --> we use col, to make matrix
            for i in range(m): #set column as zero
                matrix[i][col] = 0
