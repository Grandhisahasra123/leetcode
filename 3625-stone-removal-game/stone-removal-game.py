class Solution:
    def canAliceWin(self, n: int) -> bool:
        i = 10
        alice = True

        while i > 0:
            if n < i:
                return not alice

            n -= i
            alice = not alice
            i -= 1

        return not alice