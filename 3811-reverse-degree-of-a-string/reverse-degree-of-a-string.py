class Solution:
    def reverseDegree(self, s: str) -> int:
        result=0
        for i in range(len(s)):
            result+=(abs(ord(s[i])-ord('z'))+1)*(i+1)
        return result