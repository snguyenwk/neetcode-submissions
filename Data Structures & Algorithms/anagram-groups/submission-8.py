class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1
            anagram_dict[tuple(count)].append(string)
        
        return list(anagram_dict.values())