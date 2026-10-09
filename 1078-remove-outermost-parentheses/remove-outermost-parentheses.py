class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        c=0
        for i in range(len(s)):
            if s[i]=='(':
                if c>0:
                    ans+=s[i]
                c+=1
            else:
                c-=1
                if c>0:
                    ans+=s[i]
        return ans