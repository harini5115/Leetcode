class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        # print(ans)
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]
        return ans
        