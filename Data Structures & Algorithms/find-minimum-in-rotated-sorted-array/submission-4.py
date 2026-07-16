class Solution:
    def findMin(self, nums: List[int]) -> int:
        # get l and r pointers, while i < len(nums)
        # given a list of nums to iterate through
        # can make it more efficient by finding a middle to only parse through one side

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]