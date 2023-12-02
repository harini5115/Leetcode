class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dict_count = defaultdict(int)
        for c in chars:
            dict_count[c] +=1
        ans = 0   
        for word in words:
            flag = True
            char_count = defaultdict(int)
            for c in word:
                char_count[c] +=1
            for c in char_count.keys():
                if char_count[c]>dict_count[c]:
                    flag = False
                    break
            if flag:
                ans = ans+len(word)
        return ans
