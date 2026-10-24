class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start=max(arriveAlice,arriveBob)
        end=min(leaveAlice,leaveBob)
        if start>end:
            return 0
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        def convert(date):
            month=int(date[:2])
            day=int(date[3:])
            return sum(months[:month-1])+day
        return convert(end)-convert(start)+1
