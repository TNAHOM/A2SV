class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        output = 0

        while l <= r:
            remain = limit - people[r]
            r-=1
            output+=1
            if l <= r and remain >= people[l]:
               l+=1

        # if l == r and people[l] <= limit:
            # print(people[l])
            # output+=1
            # print(l, r)
        return output