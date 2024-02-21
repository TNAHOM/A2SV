class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        output = 0

        while target > 1:
            if maxDoubles == 0:
                output+=target-1
                target-=target+1
                
            elif target%2 == 1:
                target-=1
                output+=1

            else:
                target//=2
                maxDoubles-=1
                output+=1

        return output