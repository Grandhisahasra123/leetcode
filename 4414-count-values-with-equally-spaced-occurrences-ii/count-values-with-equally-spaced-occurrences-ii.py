class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d={}
        c=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i,]
            else:
                d[nums[i]].append(i)
        for i in d.values():
            ans=1
            if len(i)>=3:
                for j in range(len(i)-2):
                    if i[j+1]-i[j]!=i[j+2]-i[j+1]:
                        ans=0
                if ans!=0:
                    c+=1
        return c
                        