class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        tot = 0
        count = 0

        for x in nums:
            if tot >= n:
                return count
            while x > tot+1:
                print(tot)
                tot += tot+1
                count+=1

                if tot >= n:
                    return count
            if tot >= n:
                return count
            tot+=x

        while n > tot:
            # print(n, tot)
            tot += tot+1
            count+=1

        return count

            
