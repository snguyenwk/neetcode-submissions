class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_parsed = set()

        for num in nums: # iterate through nums array
            if num in nums_parsed: # check if num is already in our set
                return True # if yes, return T! we found a dupe
            nums_parsed.add(num) # if not, add num to end of set, reiterate
        return False