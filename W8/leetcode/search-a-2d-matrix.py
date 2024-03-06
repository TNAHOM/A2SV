class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ind = 0
        l, r = 0, len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] <= target:
                l = mid+1
                ind = mid
            else:
                r = mid-1
        print(ind)

        l, r = 0, len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[ind][mid] == target:
                return True
            if matrix[ind][mid] < target:
                l = mid+1
            else:
                r = mid-1

        return