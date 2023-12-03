class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurance = [-1]*26
        last_occurance = [-1]*26
        for i in range(len(s)):
            curr = ord(s[i])-ord('a')
            if first_occurance[curr]==-1:
                first_occurance[curr] = i
            last_occurance[curr]=i
        ans = 0
        for i in range(26):
            if first_occurance[i]==-1:
                continue
            between = set()
            for j in range(first_occurance[i]+1, last_occurance[i]):
                between.add(s[j])
                if len(between)>=26:
                    break
            ans +=len(between)
        return ans
 
        