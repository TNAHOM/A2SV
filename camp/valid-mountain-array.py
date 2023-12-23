class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        l = 1
        c = 0
        if arr[0] > arr[1]:
            return False

        while c < len(arr)-1:
            if arr[c] == arr[c+1] or (l == 0 and arr[c] < arr[c+1]):
                return False
            if l == 1 and arr[c] > arr[c+1]:
                l-=1
            
            c+=1

        if l == 1:
            return False
        return True