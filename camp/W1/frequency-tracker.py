class FrequencyTracker:

    def __init__(self):
        self.occurence = defaultdict(int) # all values will start from 0
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        self.occurence[number] += 1
        f = self.occurence[number]
        self.frequency[f] +=1
        self.frequency[f-1] -=1

    def deleteOne(self, number: int) -> None:
        if self.occurence[number] > 0:
            self.occurence[number] -= 1
            f = self.occurence[number]
            self.frequency[f] +=1
            self.frequency[f+1] -=1


    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)