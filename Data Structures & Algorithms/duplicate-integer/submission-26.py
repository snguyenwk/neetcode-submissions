class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # need to keep track of duplicates in an array
        # if duplicate, return True else False
        # iterate through the array, hold values in a set
        # look through set and compare with iterated num
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False