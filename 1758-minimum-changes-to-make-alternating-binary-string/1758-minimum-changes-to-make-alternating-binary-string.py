class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev1 = s[0]
        if prev1=='0':
            prev2 = '1'
        else:
            prev2 = '0'
        n1 = 0
        n2 = 1
        for i in range(1, len(s)):
            cur = s[i]
            cur1 = cur
            cur2 = cur
            if prev1==cur1:
                n1 +=1
                if cur1=='0':
                    cur1  = '1'
                else:
                    cur1 = '0'
            if prev2== cur2:
                n2 +=1
                if cur2=='0':
                    cur2 = '1'
                else:
                    cur2 = '0'
            prev1 = cur1
            prev2 = cur2
        return min(n1, n2)
                    
                