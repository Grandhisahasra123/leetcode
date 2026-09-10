def canShip(weights,days,weigh):
    s,c=0,1
    for weight in weights:
        if s+weight<=weigh:
            s+=weight
        else:
            c+=1
            s=weight
    return c<=days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canShip(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low