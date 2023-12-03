class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        ans = set()
        divisible_set = set()
        for n in nums:
            if n%p==0:
                divisible_set.add(n)
        cur = ''
        cur_div = 0
        i = 0
        j = 0
        while(i<len(nums)):
            if j<len(nums) and nums[j] in divisible_set:
                cur_div +=1
            # print(i, j, cur_div, cur, ans)
            if cur_div<=k:
                cur += '_'+str(nums[j])
                j = j+1
                ans.add(cur)
            if cur_div>k or j>=len(nums):
                i = i+1
                j = i
                cur =''
                cur_div = 0
        return len(ans)      