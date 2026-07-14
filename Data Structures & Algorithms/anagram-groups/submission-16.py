# grouping anagrams together into sublists
# return list w sublists
# need to initialize a defaultdict to hold mult k, v pairs
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())