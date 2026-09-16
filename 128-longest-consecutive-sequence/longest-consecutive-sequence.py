class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        d={}
        mx=0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for i in d:
            if i-1 not in d:
                curr=i
                c=1
                while curr+1 in d:
                    curr+=1
                    c+=1
                mx=max(mx,c)
        return mx
        