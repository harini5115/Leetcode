class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)

        def helper(val):
            l, r = 0, n - 1
            while l <= r:
                m = (l + r) // 2
                s, e, p = jobs[m]
                if s < val: l = m + 1
                else: r = m - 1
            return l

        dp = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            j = helper(jobs[i][1])
            dp[i] = max(dp[i + 1], dp[j] + jobs[i][2])
        return dp[0]