class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            add = numbers[r] + numbers[l]
            if add == target:
                return [l+1, r+1]
            if add < target:
                l+=1
            elif add > target:
                r-=1
            