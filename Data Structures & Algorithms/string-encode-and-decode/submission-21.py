class Solution:
# create string to hold encode, res
# loop and add int delimiter and symbol delimeter
# return string res
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "!" + s
        return res

# initialize i pointer, and res []
# loop through to find delimiters and append the range to result
# also need a j pointer as we need two sides
# return array res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "!":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res