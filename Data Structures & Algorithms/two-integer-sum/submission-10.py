class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                print(f"i={i}, num={num}, diff={diff}, map={map}")
                return [map[diff], i]
            map[num] = i