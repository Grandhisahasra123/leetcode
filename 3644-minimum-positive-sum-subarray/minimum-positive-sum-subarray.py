class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mn=100000000000
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                length=j-i+1
                if l<=length<=r and s>0:
                    mn=min(mn,s)
        return -1 if mn==100000000000 else mn