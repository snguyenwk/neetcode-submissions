# we need a map and a freq sublist 
# loop through nums and loop through the created count map
# append num to freq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # increment += 1 to count map
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # loop through count.items() in order to add the num/count to buckets
        for num, count in count.items():
            freq[count].append(num)
        
        # loop through freq inverse in order to get most freq numbers
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res