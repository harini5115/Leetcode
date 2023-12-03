class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        start = 0
        ans = 0
        i = 0
        while(i<len(s)):
            # print(i, chars, start)
            if s[i] in chars:
                ans = max(ans, len(chars))
                for j in range(start, i):
                    if s[j] in chars:
                        chars.remove(s[j])
                    if s[j]==s[i]:
                        break
                start = j+1
            chars.add(s[i])
            i += 1
        return max(ans, len(chars))
        