class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for i in operations:
            if i=='+':
                x1=st[-1]
                x2=st[-2]
                s=x1+x2
                st.append(s)
            elif i=='D':
                x1=st[-1]
                st.append(2*x1)
            elif i=='C':
                st.pop()
            else:
                st.append(int(i))
        return sum(st)