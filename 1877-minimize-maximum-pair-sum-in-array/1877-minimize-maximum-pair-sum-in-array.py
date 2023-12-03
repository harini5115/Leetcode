class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        ans = 0
        while(i<len(nums)//2):
            ans = max(ans, nums[i]+nums[len(nums)-i-1])
            i = i+1
        return ans

        