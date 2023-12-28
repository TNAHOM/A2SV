class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.auth={}
        self.time=timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auth[tokenId]=currentTime+self.time        

    def renew(self, tokenId: str, currentTime: int) -> None:
       
        if tokenId in self.auth and self.auth[tokenId] > currentTime:
            self.auth[tokenId]= currentTime + self.time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for value in self.auth.values():
            if value > currentTime:
                count+=1
        return count


# param_3 = obj.countUnexpiredTokens(currentTime)