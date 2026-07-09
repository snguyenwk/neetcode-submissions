# need to keep track of consecutive 1's 
# reset count if track hits a 0, hold that value and compare
# return max
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            else:
                count += 1
        
        return max(result, count)