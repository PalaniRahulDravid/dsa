class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        temp =0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    temp+=mat[i][j]
        temp2 = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j==len(mat[0])-1 and i!=j:
                    temp2+=mat[i][j]
        return temp+temp2