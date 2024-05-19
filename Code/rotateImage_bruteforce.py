class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        # dummy=[[0]*n]*n
        dummy = [[0] * n for _ in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                x=matrix[i][j]
                dummy[j][n-i-1]=x
        for i in range(n):
            for j in range(n):
                matrix[i][j] = dummy[i][j]  