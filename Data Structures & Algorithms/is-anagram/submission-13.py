class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check if lengths are not equal, if not - instant F
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} # initialize two hashmaps

        for i in range(len(s)): # for loop through range of len(s), doesnt matter which we pick between two strings
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        return True