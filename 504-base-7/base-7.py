class Solution:
    def convertToBase7(self, num: int) -> str:
        a=1
        if num==0:
            return '0'
        if num<0:
            num=-num
            a=0
        res=''
        while(num>0):
            res+=str(num%7)
            num=num//7
        if a==0:
            res+='-'
        return res[::-1]
