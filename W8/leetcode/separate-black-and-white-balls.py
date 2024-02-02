class Solution:
    def minimumSteps(self, s: str) -> int:
        num_swaps = 0
        num_zeros = 0
        for num in s[::-1]:
            if num == '0':
                num_zeros += 1
            else:
                num_swaps += num_zeros
        
        return num_swaps