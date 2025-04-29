class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]

                if curSum == target:
                    return target
                
                if abs(curSum - target) < abs(closestSum - target):
                    closestSum = curSum
                if target > curSum:
                    l += 1
                else:
                    r -= 1
        return closestSum