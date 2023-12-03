class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        idx = 0
        compare_idx = idx+1
        cur_wins = 0
        while idx<len(arr) and compare_idx<len(arr):
            if cur_wins>=k:
                return arr[idx]
            
            if arr[compare_idx]<arr[idx]:
                cur_wins +=1
                compare_idx = compare_idx+1
            else:
                cur_wins = 1
                idx = compare_idx
                compare_idx = idx+1
        return arr[idx]