class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num)):
            if int(num[(len(num)-i-1)])%2==1:
                return num[:len(num)-i]
        return ""
        