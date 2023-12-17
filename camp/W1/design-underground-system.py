class UndergroundSystem:

    def __init__(self):
        self.checkInmap = {} # id -> (startstation, time)
        self.time = {} # (start, end) -> [time, count] helps for average
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInmap[id] = (stationName, t)

    def checkOut(self, id: int, end: str, t: int) -> None:
        start, time = self.checkInmap[id]
        if (start, end) not in self.time:
            self.time[(start, end)] = [0, 0]

        self.time[(start, end)][0] += t - time # getting the time taken from start to end
        self.time[(start, end)][1] += 1 # for the lenght to average

    def getAverageTime(self, start: str, end: str) -> float:
        total, count = self.time[(start, end)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)