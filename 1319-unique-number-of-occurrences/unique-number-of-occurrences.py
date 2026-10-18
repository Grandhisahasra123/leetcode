class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=[]
        for i in d:
            if d[i] not in ans:
                ans.append(d[i])
        return len(ans)==len(d)