class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            tot = 0
            count = 1

            for i in range(len(weights)-1):
                tot+=weights[i]

                if tot+weights[i+1]>mid:
                    count+=1
                    tot = 0
            
            return days >= count
                        
        l = max(weights)
        r = sum(weights)
        
        while l <=r:
            mid = (r+l)//2
            
            if check(mid):
                r=mid-1
            else:
                l=mid+1
           
        return l


                