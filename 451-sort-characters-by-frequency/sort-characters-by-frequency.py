class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d1=sorted(d,key=lambda x:d[x],reverse=True)
        ans=''
        for i in d1:
            ans+=i*d[i]
        return ans  