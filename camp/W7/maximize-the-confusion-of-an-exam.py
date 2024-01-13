class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        size = 0
        output = 0
        n = len(answerKey)
        l = 0
        for r in range(n):
            if answerKey[r] == 'T':
                size+=1
            if size +1 == k:
                output = max(output, r-l+1)
            
            while size > k:
                if answerKey[l] == 'T':
                    size-=1
                l+=1
            output = max(output, r-l+1)
        
        l = 0
        size = 0
        for r in range(n):
            if answerKey[r] == 'F':
                size+=1
            if size +1 == k:
                output = max(output, r-l+1)
            while size > k:
                if answerKey[l] == 'F':
                    size-=1
                l+=1
            output = max(output, r-l+1)

        return output