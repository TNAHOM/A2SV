class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)//4

        l = 0
        while l< len(arr)-size:
            if arr[l] == arr[l+size]:
                return arr[l]
            l+=1

