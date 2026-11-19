class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        c,ans=1,max(2,n)
        while(ans%2!=0):
            ans=ans*c
            c+=1
        return ans
