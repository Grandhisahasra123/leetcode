class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            maxi=0
            c=0
            for x in str(i):
                if maxi<int(x):
                    maxi=int(x)
                c+=1
            ans.append(int(str(maxi)*c))
        return sum(ans)