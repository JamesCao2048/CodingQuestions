# Car Pooling
# Medium

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        overload = [0] * 1001
        for trip in trips:
            for i in range(trip[1],trip[2]):
                overload[i] += trip[0]
                if overload[i] > capacity:
                    return False
        return True