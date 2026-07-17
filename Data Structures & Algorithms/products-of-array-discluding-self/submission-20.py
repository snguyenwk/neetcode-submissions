class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a res list of [1]'s for len(nums)
        # make a prefix and postfix
        # multiply both into the res list 

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res