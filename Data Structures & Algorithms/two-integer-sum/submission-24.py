# create a map for key,value pairs to find the target
# get the difference in numbers 
# return indices
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i