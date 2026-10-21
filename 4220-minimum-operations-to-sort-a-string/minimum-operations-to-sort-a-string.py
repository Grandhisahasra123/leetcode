class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        if n==1 or s==''.join(sorted(s)):
            return 0
        if n==2:
            return -1
        mn=min(s)
        mx=max(s)
        if mn==s[0] or mx==s[-1]:
            return 1
        if mx==s[0] and mn==s[-1]:
            if s.count(mn)==1 and s.count(mx)==1:
                return 3
        return 2
        