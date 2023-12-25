class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev2 = 1
        prev1 = 1
        if s[0]=="0":
            return 0
        for i in range(1,len(s)):
            cur = 0
            # print("before", i, prev1, prev2, cur,s[i-1:i+1])
            if s[i-1:i+1]>="10" and s[i-1:i+1]<="26":
                # print("in")
                cur +=prev2
            if s[i]>='1' and s[i]<='9':
                # print("in")
                cur +=prev1
            prev2 = prev1
            prev1 = cur
            # print("after", i, prev1, prev2, cur)
        return prev1
                
        