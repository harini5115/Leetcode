class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = [[0]*len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                count = 0
                s = 0
                for row in range(i-1, i+2):
                    for col in range(j-1, j+2):
                        if 0<=row<len(img) and 0<=col<len(img[0]):
                            s +=img[row][col]
                            count +=1
                ans[i][j] = s//count
        return ans