class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        output = 0
        for x in costs:
            coins-=x
            if coins>=0:
                output+=1
            else:
                break

        return output