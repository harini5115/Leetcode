class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        count_1 = Counter(word1)
        count_2 = Counter(word2)
        for k in count_1.keys():
            if k not in count_2:
                return False
        for k in count_2.keys():
            if k not in count_1:
                return False
        values_1 = sorted(count_1.values())
        values_2 = sorted(count_2.values())
        for i in range(len(values_1)):
            if values_1[i]!=values_2[i]:
                return False
        return True
            
            
        
        