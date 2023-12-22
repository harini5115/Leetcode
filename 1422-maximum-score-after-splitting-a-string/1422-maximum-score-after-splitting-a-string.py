class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_zeros = 0
        count_ones = 0
        for c in s:
            if c=='0':
                count_zeros+=1
            else:
                count_ones+=1
        till_sum_zero = 0
        till_sum_ones = count_ones
        ans = 0
        for i in range(len(s)-1):
            if s[i]=='0':
                till_sum_zero +=1
            else:
                till_sum_ones -=1
            ans = max(ans, till_sum_zero+till_sum_ones)
        return ans
            
        