class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def compare(left, right, turn):
            if left == right:
                if turn:
                    return [nums[left], 0]
                else:
                    return [0, nums[left]]
            
            leftturn = compare(left+1, right, not turn)
            rightturn = compare(left, right-1, not turn)
            # print(leftturn)
            if turn:
                leftturn[0]+=nums[left]
                rightturn[0]+=nums[right]

                if leftturn[0] > rightturn[0]:
                    return leftturn
                return rightturn
            else:
                leftturn[1]+=nums[left]
                rightturn[1]+=nums[right]

                if leftturn[1] > rightturn[1]:
                    return leftturn
                return rightturn

        x = compare(0, len(nums)-1, True)

        return x[0] >= x[1]