# brute force can compare each and every int
# can make a hashSet to see duplicates.
# if num is in set, we can return T immediately. else F
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_in_list = set()

        for num in nums:
            if num in nums_in_list:
                return True
            nums_in_list.add(num)
        return False