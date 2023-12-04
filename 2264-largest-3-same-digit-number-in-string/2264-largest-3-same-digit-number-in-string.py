class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans = ''
        i = 0
        while(i<len(num)):
            if i+1<len(num) and i+2<len(num):
                if num[i+1]==num[i] and num[i+2]==num[i]:
                    if ans=='' or ans[0]<=num[i]:
                        ans=num[i]+num[i]+num[i]
                    i = i+2
            i =i+1
        return ans
        