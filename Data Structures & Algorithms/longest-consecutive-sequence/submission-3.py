class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set, and longest variable.
        # loop through set, if num - 1 is not in, length = 1
        # check if num + length in set
        # check max
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
