class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_matrix=[0]* len(matrix)
        col_matrix=[0]* len(matrix[0])
        row,col=len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_matrix[i]=1
                    col_matrix[j]=1
        #for col
        for i in range(row):
            if row_matrix[i]==1:
                for j in range(col):
                    matrix[i][j]=0
        #for row
        for i in range(col):
            if col_matrix[i]==1:
                for j in range(row):
                    matrix[j][i]=0            

        