# [1, 2, 3, 1, 2, 1, 1]
# need a count map to track num, value pair
# we then need a freq sublist 
# loop through initial nums array and fill key value pairs 
# then, loop through count map via items and append num to the freq
# create res array and loop from the back
# append num to res array
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res