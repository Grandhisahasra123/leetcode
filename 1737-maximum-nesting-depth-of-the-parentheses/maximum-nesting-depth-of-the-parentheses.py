class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        s1=[]
        for i in s:
            if i=='(':
                s1.append(i)
            elif i==')':
                s1.pop()
            maxi=max(len(s1),maxi)
        return maxi