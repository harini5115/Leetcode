class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix)==0:
            return 0
        if len(matrix)==1:
            return min(matrix[0])
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix[1]))]
        for j in range(len(dp[0])):
            dp[0][j] = matrix[0][j]
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] = dp[i-1][j]
                if j!=0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                if j!=len(dp[0])-1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                dp[i][j] = dp[i][j]+matrix[i][j]
        return min(dp[len(matrix)-1])
                
        
        