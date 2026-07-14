# prog that sees if two strings are anagrams
# if len s != len t, return F
# create an array of count to store values of letters seen
# second loop to track values, if !=, return F
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for value in count:
            if value != 0:
                return False
        return True