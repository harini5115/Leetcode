class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        row_count = [0]*len(bank)
        for i in range(len(bank)):
            row_count[i] = sum([1 if x=='1' else 0 for x in bank[i]])
        ans = 0   
        prev = 0
        while(prev<len(row_count) and row_count[prev]==0):
            prev +=1
        
        nex = prev+1
        while(nex<len(row_count)):
            while(nex<len(row_count) and row_count[nex]==0):
                nex +=1
        
            if nex<len(row_count):
                ans +=row_count[prev]*row_count[nex]
                prev = nex
                nex = nex+1
        return ans
        
            
            
        