class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        ans=n*n*w
        if ans<=maxWeight:
            return n*n
        else:
            return maxWeight//w