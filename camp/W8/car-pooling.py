class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        get_size = 0
        for num, f, t in trips:
            get_size = max(get_size, t)

        output = [0 for _ in range(get_size+1)]

        for num, f, t in trips:
            output[f]+=num
            output[t]-=num
        print(output)
        curr = 0
        for x in range(len(output)):
            curr+=output[x]
            print(curr, '--')
            if curr > capacity:
                return False
            output[x] = curr
        
        return True