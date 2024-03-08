class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations)-1

        find = 0

        while low <= high:
            mid = (high+low)//2
            
            if citations[mid] >= len(citations)-mid:
                high = mid-1
                find = len(citations) - mid
            else:
                low = mid+1

        return find