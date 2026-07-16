# kadane's - if your running total turns negative, set curSum to zero.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSub = 0, nums[0]
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(curSum, maxSub)
        return maxSub