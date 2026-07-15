# create set to find duplicate
# loop through nums 
# check if your num is already in set
# return bools
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False