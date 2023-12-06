class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        largest = max(candies)
        bool_candies = []

        for x in range(len(candies)):
            if candies[x] + extraCandies >= largest:
                bool_candies.append(True)
            else:
                bool_candies.append(False)
        
        return bool_candies