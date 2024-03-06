# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        find = 0
        while l<=r:
            mid = (r+l)//2
            # print(mid)

            if not isBadVersion(mid):
                l = mid+1
            elif isBadVersion(mid):
                r = mid-1
                find = mid

        return find