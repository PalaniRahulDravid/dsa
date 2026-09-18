class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        temp=0
        for i in range(len(mat)):
            temp+=mat[i][i]
            if i != len(mat)-1-i:
                temp+=mat[i][len(mat)-1-i]
        return temp
