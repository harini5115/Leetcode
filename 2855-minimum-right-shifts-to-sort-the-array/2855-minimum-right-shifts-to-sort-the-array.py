class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_min(nums):
            min_idx = 0
            for i in range(len(nums)):
                if nums[i]<nums[min_idx]:
                    min_idx = i
            return min_idx
        
        def check_sorted_till_min(nums, min_idx):
            for i in range(min_idx-1):
                if nums[i]>nums[i+1]:
                    return False
            return True
        def check_sorted_right(nums, min_idx):
            for i in range(min_idx, len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
            return True
        min_idx = get_min(nums)
        if min_idx == 0:
            if check_sorted_right(nums, min_idx):
                return 0
            return -1
        
        if (min_idx>0):
            if (nums[-1]>nums[0]) or not check_sorted_till_min(nums, min_idx) or not check_sorted_right(nums, min_idx): 
                return -1
            print(len(nums), min_idx)
            return len(nums)-min_idx
        