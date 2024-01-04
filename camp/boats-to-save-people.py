class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        output = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                output+=1
                l+=1
                r-=1
            else:
                output+=1
                r-=1

        # if l == r and people[l] <= limit:
            # print(people[l])
            # output+=1
            # print(l, r)
        return output