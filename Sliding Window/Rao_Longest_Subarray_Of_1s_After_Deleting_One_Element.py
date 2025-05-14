class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 0
        l = 0
        zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r - l + 1 - zeros)
        
        return res - 1 if res == len(nums) else res