class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cp = cardPoints
        size = 0
        l, r = 0, len(cp)-k
        tempsum = sum(cp[r:])
        output = tempsum

        l = 0
        while r < len(cp):
            tempsum += (-cp[r]) + cp[l]
            output = max(output, tempsum)
            l+=1
            r+=1
        return output