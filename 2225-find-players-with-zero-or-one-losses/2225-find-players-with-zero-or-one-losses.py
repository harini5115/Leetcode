class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import Counter
        losses = Counter([match[1] for match in matches])
        only_one_loss = []
        for loss,count in losses.items():
            if count==1:
                only_one_loss.append(loss)
        wins = set()
        for match in matches:
            if match[0] not in losses:
                wins.add(match[0])
        return sorted(list(wins)), sorted(only_one_loss)
        