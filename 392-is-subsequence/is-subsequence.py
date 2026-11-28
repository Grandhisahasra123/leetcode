class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j,c=0,0,0
        while i<len(s) and j<len(t):
            while j<len(t) and s[i]!=t[j]:
                j+=1
            while i<len(s) and j<len(t) and s[i]==t[j]:
                i+=1
                j+=1
                c+=1
        if c==len(s):
            return True
        return False
