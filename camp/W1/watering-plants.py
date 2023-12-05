class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        output = 0

        fill = 0
        temp = capacity
        while fill < len(plants):
            print(fill, output, temp)
            temp-=plants[fill]
            if temp >= 0:
                output+=1
                fill+=1
            else:
                output+=fill
                temp = capacity
                temp-=plants[fill]
                fill+=1
                output+=fill
                # fill+=1

        return output
                
