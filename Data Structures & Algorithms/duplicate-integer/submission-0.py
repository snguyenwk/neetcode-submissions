# return T if a value occurs > 1, else F
# seeing if a value has a duplicate in the array
# create a set to compare w/ in
# add num to set to keep comparing
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False