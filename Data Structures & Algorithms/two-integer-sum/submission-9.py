class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
                print(diff)
                print(map[diff])
            map[num] = i