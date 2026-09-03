class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        lst=[]
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        while(k>0):
            m,n=0,0
            for key,v in d.items():
                if m<v:
                    m=v
                    n=key
            lst.append(n)
            d.pop(n)
            k-=1
        return lst