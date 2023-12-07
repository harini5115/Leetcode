class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j-1>=0 and j<i: 
                    
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
                elif j-1<0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
        return min(dp[len(triangle)-1])