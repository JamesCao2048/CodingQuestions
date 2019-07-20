# Car Pooling
# Medium

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        getMap = {}
        leaveMap = {}
        maxStation = 0
        for trip in trips:
            if not trip[1] in getMap:
                getMap[trip[1]] = [trip[0]]
            else:
                getMap[trip[1]].append(trip[0])
            if not trip[2] in leaveMap:
                leaveMap[trip[2]] = [trip[0]]
            else:
                leaveMap[trip[2]].append(trip[0])
            maxStation = max(trip[2], maxStation)
        curPeople = 0
        for i in range(maxStation+1):
            if i in getMap:
                curPeople += sum(getMap[i])
            if i in leaveMap:
                curPeople -= sum(leaveMap[i])
            if curPeople > capacity:
                return False
        return True