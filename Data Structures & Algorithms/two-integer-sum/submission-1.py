# return i and j indices so they equal target
# can't equal eachother
# return ans with smaller index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # key, value i.e i, j

        for i, num in enumerate(nums):
            diff = target - num # you want to find that number that fits the equation: target = diff + num in index
            if diff in map:
                return [map[diff], i]
            map[num] = i
