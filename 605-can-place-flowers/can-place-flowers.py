class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        c=0
        l=len(flowerbed)
        if n==0:
            return True
        for i in range(l):
            if flowerbed[i]==0:
                if(flowerbed[i-1]!=1 or i==0) and (i==l-1 or flowerbed[i+1]!=1):
                    c+=1
                    flowerbed[i]=1
                    if c>=n:
                        return True
        return False