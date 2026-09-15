class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre=[0]
        su=0
        for i in gain:
            su+=i
            pre.append(su)
        return max(pre)
