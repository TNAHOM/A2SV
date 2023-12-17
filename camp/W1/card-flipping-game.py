class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        for x in range(len(fronts)):
            if fronts[x] == backs[x]:
                same.add(fronts[x])
        
        output = float('inf')
        for number in (fronts + backs):
            if number not in same:
                output = min(output, number)
        
        return output if output!= float('inf') else 0
