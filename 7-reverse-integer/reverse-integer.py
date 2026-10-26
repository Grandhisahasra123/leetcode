class Solution:
    def reverse(self, x: int) -> int:
        a=x
        if x<0:
            x=-x
        c=int(str(x)[::-1])
        if a<0:
            c=-c
        if -2**31<=c<=2**31:
            return c
        return 0