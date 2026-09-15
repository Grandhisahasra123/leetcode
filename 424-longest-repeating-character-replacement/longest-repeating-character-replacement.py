class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        left,mx,freq=0,0,0
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            freq=max(freq,d[s[right]])
            while (right-left+1)-freq>k:
                d[s[left]]-=1
                if d[s[left]]==0:
                    d.pop(s[left])
                left+=1
            mx=max(mx,right-left+1)
        return mx