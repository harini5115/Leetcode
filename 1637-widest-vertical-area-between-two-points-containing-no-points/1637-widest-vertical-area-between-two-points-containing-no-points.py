class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        ans = 0
        for i in range(len(points)):
            if i+1<len(points):
                ans = max(ans, points[i+1][0]-points[i][0])
        return ans
        