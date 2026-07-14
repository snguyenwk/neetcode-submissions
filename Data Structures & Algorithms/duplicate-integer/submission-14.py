# if there is a duplicate, we need a set. no need for map as we dont need k, v pair.
# return True on first duplicate
# initialize set to hold numbers as we loop.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False