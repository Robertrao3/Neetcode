class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        count = 0

        for a, b in dominoes:
            key = tuple(sorted((a,b)))
            count += freq[key]
            freq[key] += 1
        return count