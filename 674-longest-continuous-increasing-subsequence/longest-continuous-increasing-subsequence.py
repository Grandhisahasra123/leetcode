class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c,mx=1,1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c+=1
            else:
                mx=max(c,mx)
                c=1
        return max(mx,c)