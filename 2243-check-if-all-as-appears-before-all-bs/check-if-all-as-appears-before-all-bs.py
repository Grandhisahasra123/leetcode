class Solution:
    def checkString(self, s: str) -> bool:
        seen=False
        for ch in s:
            if ch=='b':
                seen=True
            elif ch=='a' and seen:
                return False
        return True