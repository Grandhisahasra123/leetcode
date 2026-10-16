class Solution:
    def maxPower(self, s: str) -> int:
        c,mx=1,1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                mx=max(mx,c)
                c=1
        return max(mx,c)
