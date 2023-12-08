class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid)==0:
            return 0
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    continue
                if i-1>=0 and j-1>=0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                elif i-1>=0 and j-1<0:
                    dp[i][j] = dp[i-1][j]
                elif i-1<0 and j-1>=0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 1
        
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
        