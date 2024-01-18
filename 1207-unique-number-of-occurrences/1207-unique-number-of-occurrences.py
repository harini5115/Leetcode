class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        present = set()
        for v in count.values():
            if v in present:
                return False
            present.add(v)
        return True
        