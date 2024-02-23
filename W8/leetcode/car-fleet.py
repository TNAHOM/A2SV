class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lane = [(position[x], speed[x]) for x in range(len(position))]
        lane.sort()
        time = []

        for x in range(len(lane)):
            time.append((target - lane[x][0])/lane[x][1])
            
        stack = []
        for x in time:
            while stack and stack[-1] <= x:
                stack.pop()
            stack.append(x)

        return len(stack)