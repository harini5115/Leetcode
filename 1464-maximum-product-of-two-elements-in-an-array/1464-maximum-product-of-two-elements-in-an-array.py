class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        m1,m2 = nums[0], nums[1]

        for i in range(2,len(nums)):
            if m1<m2:
                m1, m2 = m2, m1
            if m2<nums[i]:
                m2 = nums[i]
        return (m1-1)*(m2-1)        