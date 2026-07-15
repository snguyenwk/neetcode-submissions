class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create map
        map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i