class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k % n

        def reverse_nums(array, start, end):
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

        #Reverse whole array
        reverse_nums(nums, 0, n - 1)

        #reverse first k elements
        reverse_nums(nums, 0, k - 1)

        #reverse the rest of the array
        reverse_nums(nums, k, n - 1)