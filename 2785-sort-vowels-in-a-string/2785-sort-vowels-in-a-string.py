class Solution:
    def sortVowels(self, s: str) -> str:
        ans = ['']*len(s)
        count = defaultdict(int)
        volwels = ['A','E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if s[i] in volwels:
                count[s[i]] +=1
        cur_vowel_idx = 0
        for i in range(len(s)):
            if s[i] not in volwels:
                ans[i] = s[i]
            else:
                while(count[volwels[cur_vowel_idx]]==0):
                    cur_vowel_idx=cur_vowel_idx+1
                ans[i] = volwels[cur_vowel_idx]
                count[volwels[cur_vowel_idx]] -=1
        return ''.join(ans)


            

        