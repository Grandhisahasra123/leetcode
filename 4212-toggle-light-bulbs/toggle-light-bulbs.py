class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d={}
        for i in range(len(bulbs)):
            if bulbs[i] not in d:
                d[bulbs[i]]=1
            else:
                d[bulbs[i]]+=1
        ans=[]
        for key,value in d.items():
            if value%2==1:
                ans.append(key)
        return sorted(ans)