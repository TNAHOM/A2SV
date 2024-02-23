class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        bini = []
        stack = []
        temp = float("inf") 
        for num in nums:
            bini.append(temp)
            temp = min(temp,num)
        
        # print(bini)
        for x in range(len(nums)-1, -1, -1):
            while stack and stack[-1][1] < nums[x]:
                index,curr_val = stack.pop()
                # print(bini[index], curr_val, '-->', nums[x])
                if curr_val > bini[x]:
                    return True
            stack.append((x,nums[x]))
        return False

