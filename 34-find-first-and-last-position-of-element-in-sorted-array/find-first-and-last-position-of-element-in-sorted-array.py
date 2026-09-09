class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = bisect_left(nums,target)
        last = bisect_right(nums,target)
        if first==last:
            return [-1,-1]
        else:
            return[first,last-1]
                