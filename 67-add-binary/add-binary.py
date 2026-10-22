def convert(a):
    c,l=0,0
    a=int(a)
    while(a>0):
        l+=(a%10)*(2**c)
        c+=1
        a=a//10
    return l
def con(ans):
    if ans==0:
        return '0'
    l=''
    while(ans>0):
        l+=str(ans%2)
        ans=ans//2
    return l[::-1]
class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        c=convert(a)
        d=convert(b)
        ans=c+d
        return con(ans)