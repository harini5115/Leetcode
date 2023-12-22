class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        pointer = 0
        i = 0
        while(pointer<len(arr)):
            i = i+1
            if arr[pointer]!=i:
                k -=1
            else:
                pointer +=1
            if k==0:
                return i
        if k==0:
            return i
        if k>0:
            return i+k
                
                
        