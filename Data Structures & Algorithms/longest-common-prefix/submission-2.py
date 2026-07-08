# return longest common prefix
# if none, return empty string ""
# we need to parse all strings and track until the prefix changes
# track with a set? use in?
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]