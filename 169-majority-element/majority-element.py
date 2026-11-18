class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for k,v in d.items():
            if v>n//2:
                return k