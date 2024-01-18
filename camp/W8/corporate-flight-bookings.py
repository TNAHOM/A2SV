class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0 for _ in range(n+1)]
        print(output)
        for f, l, k in bookings:
            output[f-1] +=k
            output[l] -=k
        tot = 0
        for x in range(len(output)):
            tot+=output[x]
            output[x] = tot
        
        return output[:n]