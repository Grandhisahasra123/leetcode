class Solution:
    def reverseParentheses(self, s: str) -> str:
        s1=[]
        for i in s:
            if i!=')':
                s1.append(i)
            else:
                a=''
                while(s1[-1]!='('):
                    a+=s1.pop()
                s1.pop()
                for i in a:
                    s1.append(i)
        return ''.join(s1)