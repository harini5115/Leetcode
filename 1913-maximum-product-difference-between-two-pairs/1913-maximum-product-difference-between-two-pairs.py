class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, min1, min2 = 0, 0, sys.maxsize, sys.maxsize
        for n in nums:
            if n>max1:
                max2 = max1
                max1 = n
            else:
                max2 = max(max2, n)
            if n<min1:
                min2 = min1
                min1 = n
            else:
                min2 = min(min2, n)
        return max1*max2 - min1*min2
      