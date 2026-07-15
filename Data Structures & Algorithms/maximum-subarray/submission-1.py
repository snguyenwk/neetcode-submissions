class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # create curSub and maxSub in order to track the int. if curSub < 0, iterate next and set
        # curSub to 0
        curSum, maxSub = 0, nums[0]
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub