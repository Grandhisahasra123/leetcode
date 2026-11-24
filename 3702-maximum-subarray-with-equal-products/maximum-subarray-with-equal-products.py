class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            l,g,p=1,0,1
            for j in range(i,n):
                p*=nums[j]
                l=lcm(l,nums[j])
                g=gcd(g,nums[j])
                if p==l*g:
                    c=max(c,j-i+1)
        return c