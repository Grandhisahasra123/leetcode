class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=(num//2)+1
        if num==1:
            return True
        while low<=high:
            mid=(low+high)//2
            if mid*mid>num:
                high=mid-1
            elif mid*mid==num:
                return True
            else:
                low=mid+1
        return False
        