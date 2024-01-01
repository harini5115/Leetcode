class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_pointer = 0
        s_pointer = 0
        while g_pointer<len(g) and s_pointer<len(s):
            if g[g_pointer]<=s[s_pointer]:
                g_pointer +=1
                s_pointer +=1
            else:
                s_pointer +=1
        return g_pointer
        