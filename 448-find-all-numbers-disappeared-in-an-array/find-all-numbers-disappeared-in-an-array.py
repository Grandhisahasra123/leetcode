class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lst=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                lst.append(i)
        return lst