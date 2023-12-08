class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        prev1, prev2=1,1
        for i in range(2,n+1):
            s = prev1+prev2
            prev1=prev2
            prev2=s
        return prev2

        