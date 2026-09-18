class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        open_b="([{"
        close_b=")]}"
        d=dict(zip(close_b,open_b))
        for i in s:
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            else:
                if not st:
                    return False
                if d[i]==st[-1]:
                    st.pop()
                else:
                    return False
        return len(st)==0