class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect_left(arr, x)
        l = ind-1
        r = ind

        while (r-l)<=k:
            if r>=len(arr) or (l>=0 and abs(arr[l]-x) <= abs(arr[r]-x)):
                l-=1
            else:
                r+=1

        return arr[l+1:r]
