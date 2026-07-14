class Solution:

# initialize res string
# loop through strs
# add int, delimeter, and string
# return res string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

# initialize res list and i pointer
# also need a j pointer. we will be returning ranges to capture length
# initalize length
# return res list
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res