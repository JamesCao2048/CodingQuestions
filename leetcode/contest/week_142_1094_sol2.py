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
        final_cap = capacity
        for trip in trips:
            if trips[2] - trips[1] < 500:
                for i in range(trip[1],trip[2]):
                    overload[i] += trip[0]
                    if overload[i] > final_cap:
                        return False
            else:
            # 针对trip跨度较长的case做的hack优化
                for i in range(trip[1]):
                    overload[i] -= trip[0]
                for i in range(trip[2],1001):
                    overload[i] -= trip[0]
                final_cap -= trip[0]
        if [i for i in overload if i > final_cap]:
            return False
        return True