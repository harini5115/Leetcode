class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left, right = [None] * n, [None] * n 

        # Use list as stack
        s1, s2 = [], [] 

        # getting number of element strictly 
        # larger than A[i] on Left. 
        for i in range(0, n): 
            cnt = 1

            # get elements from stack until 
            # element greater than A[i] found 
            while len(s1) > 0 and s1[-1][0] > A[i]: 
                cnt += s1[-1][1] 
                s1.pop() 

            s1.append([A[i], cnt]) 
            left[i] = cnt 

        # getting number of element
        # larger than A[i] on Right. 
        for i in range(n - 1, -1, -1): 
            cnt = 1

            # get elements from stack until 
            # element greater or equal to A[i] found 
            while len(s2) > 0 and s2[-1][0] >= A[i]: 
                cnt += s2[-1][1] 
                s2.pop() 

            s2.append([A[i], cnt]) 
            right[i] = cnt 

        result = 0

        # calculating required resultult 
        for i in range(0, n): 
            result += A[i] * left[i] * right[i] 
            result = result%(pow(10,9)+7)

        return result 
        