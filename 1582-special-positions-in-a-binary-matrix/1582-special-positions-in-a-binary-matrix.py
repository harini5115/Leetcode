class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if len(mat)==0:
            return 0
        col_sum = [0]*len(mat[0])
        row_sum = [0]*(len(mat))
        for i in range(len(mat)):
            row_sum[i] = sum(mat[i])
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                col_sum[j] = col_sum[j]+mat[i][j]
        # print(row_sum)
        # print(col_sum)
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # print(i,j, mat[i][j], row_sum[i], col_sum[j])
                if mat[i][j]==1 and row_sum[i]==1 and col_sum[j]==1:
                    ans = ans+1
        return ans
        