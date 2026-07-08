# return i and j indices so they equal target
# can't equal eachother
# return ans with smaller index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # need key, value

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
