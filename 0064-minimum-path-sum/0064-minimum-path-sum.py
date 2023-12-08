class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i-1>=0 and j-1>=0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
                elif i-1>=0 and j-1<0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                elif i-1<0 and j-1>=0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                else:
                    dp[i][j] = grid[i][j]
        return dp[len(grid)-1][len(grid[0])-1]
                
        