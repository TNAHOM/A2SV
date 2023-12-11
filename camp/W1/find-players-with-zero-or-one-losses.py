class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        status = {}

        for x in matches:
            for y in x:
                if y not in status.keys():
                    status[y] = [0, 0]

                if x[0] == y:
                    status[y][0]+=1
                else:
                    status[y][1]+=1
        won = sorted([key for key, value in status.items() if value[1] == 0])
        loss = sorted([key for key, value in status.items() if value[1] == 1])
        return [won, loss]
            
