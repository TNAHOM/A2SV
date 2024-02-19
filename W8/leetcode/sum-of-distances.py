class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        sum_left = defaultdict(int)
        occu_left = defaultdict(int)

        for i, x in enumerate(nums):
            res[i] -= sum_left[x]
            res[i] += occu_left[x]*i

            sum_left[x] += i
            occu_left[x] += 1
        
        sum_right = defaultdict(int)
        occu_right = defaultdict(int)

        for i, x in reversed(list(enumerate(nums))):
            res[i] += sum_right[x]
            res[i] -= occu_right[x]*i

            sum_right[x] += i
            occu_right[x] += 1
        
        return res