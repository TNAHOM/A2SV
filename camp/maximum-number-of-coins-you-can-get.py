class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        l = 1
        r = len(piles)-1
        output = []
        while l < r:
            output.append(piles[l])
            l+=2
            r-=1
        return sum(output)