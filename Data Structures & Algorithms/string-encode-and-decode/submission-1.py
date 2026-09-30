class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        encodeStr = ""
        for s in strs:
            encodeStr += str(len(s)) + "#" + s
        return encodeStr



    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length

            result.append(s[i:j])

            i = j
        
        return result