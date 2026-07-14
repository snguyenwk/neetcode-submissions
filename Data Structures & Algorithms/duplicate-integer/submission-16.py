# create set to track duplicate values
# loop through nums, if num is seen already, return T
# else return F
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False