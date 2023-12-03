class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        while i<len(nums):
            if nums[i]!=0:
                i = i+1
                continue
            j = max(j, i+1)
            while(j<len(nums)):
                if nums[j]!=0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j +=1
            i = i+1
        