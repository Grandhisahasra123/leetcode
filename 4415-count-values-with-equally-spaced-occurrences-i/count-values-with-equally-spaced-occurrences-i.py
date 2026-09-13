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
            if len(i)==3 and i[1]-i[0]==i[2]-i[1]:
                c+=1
        return c
