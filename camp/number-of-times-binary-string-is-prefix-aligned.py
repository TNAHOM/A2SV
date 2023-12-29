class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        output = 0
        val = 0
        ind = 0

        for x in range(len(flips)):
            val+=flips[x]
            ind+=x+1

            if val == ind:
                output+=1
        
        return output