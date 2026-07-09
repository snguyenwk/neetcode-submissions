# using defaultdict here to group strings into sublists.
# can output  as a list in any order
# must be anagrams
# break down strs list into strings - create a count array 
# break down strings in chars - iterate 1 into the count array according to ord (ascii)
# append the string to the result hashmap
# return the values from result
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for chars in string:
                count[ord(chars) - ord('a')] += 1
            grouped[tuple(count)].append(string)
        return list(grouped.values())