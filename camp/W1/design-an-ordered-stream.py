class OrderedStream:

    def __init__(self, n: int):
        self.output = [0]*(n+1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        pt = 0
        self.output[idKey] = value

        new = []
        while  self.pointer < len(self.output) and self.output[self.pointer]:
            new.append(self.output[self.pointer])
            self.pointer+=1
        
        return new


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)