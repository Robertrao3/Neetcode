class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxN = max(nums)
        count = 0
        l = 0
        maxfound = 0

        for r in range(len(nums)):
            if nums[r] == maxN:
                maxfound += 1
            
            while maxfound == k:
                count += len(nums) - r
                if nums[l] == maxN:
                    maxfound -= 1
                l += 1
        return count