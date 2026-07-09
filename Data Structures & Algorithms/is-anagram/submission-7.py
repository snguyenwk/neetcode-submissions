# return false if strings are not same len
# create two hashmaps to track count of string S and T
# increment by 1 after iterating through both strings
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stringS, stringT = {}, {}

        for i in range(len(s)):
            stringS[s[i]] = stringS.get(s[i], 0) + 1
            stringT[t[i]] = stringT.get(t[i], 0) + 1

        for c in stringS:
            if stringS[c] != stringT.get(c, 0):
                return False
        return True