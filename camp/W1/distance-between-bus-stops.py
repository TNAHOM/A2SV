class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """

        if start > destination:
            start, destination = destination, start

        cw = sum(distance[start:destination])
        if start == 0:
            ccw = sum(distance[destination:])
        else:
            ccw = sum(distance[:start]) + sum(distance[destination:])
        print(cw, ccw)
        return min(cw, ccw)