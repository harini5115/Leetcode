class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0]+nums+[sys.maxsize]
        n = len(nums)
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                break
        else:
            return (n-2)*(n-1)//2
        for j in range(n-1, 0, -1):
            if nums[j-1] >= nums[j]:
                break
        l = 0
        r = j
        res = 0
        while l <= i:
            while r < n and nums[l] >= nums[r]:
                r += 1
            res += n - r
            l += 1
        return res