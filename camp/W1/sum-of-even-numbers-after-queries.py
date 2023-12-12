class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic = {}
        output = []
        even_sum = 0

        for x in range(len(nums)):
            dic[x] = nums[x]
            if nums[x]%2==0:
                even_sum+=nums[x]
        
        for y, z in queries:
            get = dic[z]
            add = get + y
            dic[z] = add

            if add%2==0 and get%2==1:
                even_sum+=add
                output.append(even_sum)
            elif add%2==0 and get%2==0:
                even_sum+=(add-get)
                output.append(even_sum)
            elif add%2==1 and get%2==0:
                even_sum-=get
                output.append(even_sum)
            elif add%2==1 and get%2==1:
                output.append(even_sum)

            
        return output