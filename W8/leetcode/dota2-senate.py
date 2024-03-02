class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        
        container = []
        stack = []

        R = senate.count('R')
        D = senate.count('D')

        for x in senate:
            if stack and stack[-1] != x:
                senate.append(stack.pop())

                if x == 'D': D-=1
                if x == 'R': R-=1
            else:
                stack.append(x)
            if R == 0:
                return 'Dire'
            elif D == 0:
                return 'Radiant'