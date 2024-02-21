class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        output = 0
        for x in range(len(costs)//2):
            output+=costs[x][0]
        
        for x in range(len(costs)//2, len(costs)):
            output+=costs[x][1]

        return output