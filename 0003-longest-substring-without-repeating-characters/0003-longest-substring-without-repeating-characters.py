class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in chars:
                # print(i, start, ans, i-start)
                ans = max(ans, i-start)
                prev_start = start
                start = chars[s[i]]+1
                for j in range(prev_start, start):
                    if s[j] in chars:
                        del chars[s[j]]
            elif i==len(s)-1:
                ans= max(ans, i-start+1)
            chars[s[i]]=i
        return ans
        