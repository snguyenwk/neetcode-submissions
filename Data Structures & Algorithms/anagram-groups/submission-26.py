class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create defaultdict, store multiple ana groups
        # parse string and chars
        # map string to dict

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())