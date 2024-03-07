class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        find = 0
        
        while low<=high:
            mid = (low+high)//2
            tot = 0
            for x in piles: tot+=ceil(x/mid)
            # print(mid, tot)
            if tot<=h:
                high = mid-1
                find = mid
            else:
                low = mid+1

        return find