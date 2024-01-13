class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        s_count = Counter(s)
        t_count = Counter(t)
        ans = 0
        for k in s_count.keys():
            if k not in t_count:
                ans += s_count[k]
            else:
                ans += max(s_count[k]-t_count[k], 0)
        return ans
        