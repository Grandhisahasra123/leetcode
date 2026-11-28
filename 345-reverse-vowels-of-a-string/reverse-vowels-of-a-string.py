class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        a=list(s)
        i,j=0,len(s)-1
        while i<j:
            while i<j and a[i] not in vowels:
                i+=1
            while i<j and a[j] not in vowels:
                j-=1
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        return ''.join(a)