class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return False
        count = Counter(arr)
        frequency = list(count.values())
        return len(frequency) == len(set(frequency))        