class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        a=abs(nums[-1]-nums[2])
        b=abs(nums[-2]-nums[1])
        c=abs(nums[-3]-nums[0])
        return min(a,b,c)
