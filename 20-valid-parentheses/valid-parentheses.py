class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            else:
                if not st:
                    return False
                if (st[-1]=='{' and i=='}') or(st[-1]=='[' and i==']') or (st[-1]=='(' and i==')') :
                    st.pop()
                else:
                    return False
        return len(st)==0