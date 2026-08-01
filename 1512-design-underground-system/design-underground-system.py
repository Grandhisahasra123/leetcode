class UndergroundSystem:

    def __init__(self):
        self.d1={}
        self.d2={}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d1[id]=(stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation,starttime=self.d1.pop(id)
        trip = (startstation,stationName)
        if trip in self.d2:
            self.d2[trip][0]+=(t-starttime)
            self.d2[trip][1]+= 1
        else:
            self.d2[trip]=[t-starttime,1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation,endStation)
        return self.d2[trip][0]/self.d2[trip][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)