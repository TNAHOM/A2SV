class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        tot = numOnes + numZeros + numNegOnes
        sum_ = 0

        for x in range(k):
            if numOnes != 0:
                numOnes-=1
                sum_+=1
            elif numZeros != 0:
                numZeros-=1
            elif numNegOnes != 0:
                numNegOnes-=1
                sum_-=1
        
        return sum_