class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    #for col -1
                    for k in range(row):
                        if matrix[k][j]!=0:
                            matrix[k][j]="-1"
                    #for row -1
                    for l in range(col):
                        if matrix[i][l]!=0:
                            matrix[i][l]="-1"
        for i in range(row):
            for j in range(col): 
                if matrix[i][j]=="-1":  
                    matrix[i][j]=0                        
        