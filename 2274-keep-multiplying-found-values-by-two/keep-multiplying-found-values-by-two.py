class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        while(original in d):
            original=2*original
        return original