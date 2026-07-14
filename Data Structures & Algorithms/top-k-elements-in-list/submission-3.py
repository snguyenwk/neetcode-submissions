# [1, 2, 3, 1, 2, 1, 1]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # [[], [], [], [], [], [], [], []]
        #  0   1   2   3   4   5   6   7 
        for num in nums:
            count[num] = count.get(num, 0) + 1
            # {1: 4, 2: 2, 3: 1}
        for num, c in count.items():
            freq[c].append(num)
            # freq[4].append(1)
            # freq[2].append(2)
            # freq[1].append(3)
            # [[], [3], [2], [], [4], [], [], []]
            #  0   1    2    3   4    5   6   7
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res