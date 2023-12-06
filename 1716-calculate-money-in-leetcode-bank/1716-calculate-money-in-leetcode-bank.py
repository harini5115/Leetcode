class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        n_div = n//7
        ans += ((n_div)*(n_div-1)//2)*7+(7*4)*n_div
        n_rem = n%7
        for i in range(n_rem):
            ans +=n_div+i+1
        return ans
        