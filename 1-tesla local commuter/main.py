import math


class Solution:
    def __init__(self, inputs):
        self.map = dict()
        for input in inputs:
            start = input[0]
            end = input[1]
            distance = input[2:]
            if not start in self.map.keys():
                self.map[start] = dict()
            self.map[start][end] = int(distance)

    def calculateRoute(self, route):
        stops = route.split('-')
        distance = 0
        for index in range(len(stops)-1):
            start = stops[index]
            end = stops[index+1]
            if start in self.map.keys()\
                    and end in self.map[start].keys():
                distance += self.map[start][end]
            else:
                return -1
        return distance

    def getNumberOfTripsWithLimitStops(self, start, end, limit, paths):
        if limit > 0:
            count = 0
            paths.append(start)
            if start in self.map.keys():
                for nexts in self.map[start].keys():
                    if nexts == end:
                        count += 1
                        paths.append(end)
                        print(paths)
                        paths.pop()
                    else:
                        count = count + self.getNumberOfTripsWithLimitStops(nexts, end, limit - 1, paths)
            paths.pop()
            return count
        else:
            return 0

    def getNumberOfTripsWithExactStops(self, start, end, limit, paths):
        if limit > 0:
            count = 0
            paths.append(start)
            if start in self.map.keys():
                for nexts in self.map[start].keys():
                    if limit == 1:
                        if nexts == end:
                            count += 1
                            paths.append(end)
                            print(paths)
                            paths.pop()
                    else:
                        count = count + self.getNumberOfTripsWithExactStops(nexts, end, limit - 1, paths)
            paths.pop()
            return count
        else:
            return 0

    def getShortestRoute(self, start, end, current, shortest, visited, paths):
        if current < shortest:
            paths.append(start)
            if start in self.map.keys():
                for nexts in self.map[start].keys():
                    if nexts == end:
                        if current + self.map[start][nexts] < shortest:
                            shortest = current + self.map[start][nexts]
                        paths.append(end)
                        print(paths)
                        paths.pop()
                    else:
                        if nexts not in visited:
                            visited.append(nexts)
                            updated = self.getShortestRoute(nexts, end, current + self.map[start][nexts], shortest, visited, paths)
                            visited.pop()
                            if updated < shortest:
                                shortest = updated
            paths.pop()
        return shortest

    def getNumberOfTripsWithLimitDistance(self, start, end, limit, paths):
        if limit > 0:
            count = 0
            paths.append(start)
            if start in self.map.keys():
                for nexts in self.map[start].keys():
                    if nexts == end:
                        if self.map[start][nexts] <= limit:
                            count += 1
                            paths.append(end)
                            print(paths)
                            paths.pop()
                    count = count + self.getNumberOfTripsWithLimitDistance(nexts, end, limit - self.map[start][nexts], paths)
            paths.pop()
            return count
        else:
            return 0


inputs = [
    "AB5",
    "BC4",
    "CD8",
    "DC8",
    "DE6",
    "AD5",
    "CE2",
    "EB3",
    "AE7",
]

routes = [
    "A-B-C",
    "A-D",
    "A-D-C",
    "A-E-B-C-D",
    "A-E-D",
]

sol = Solution(inputs)

for route in routes:
    distance = sol.calculateRoute(route)
    if distance >= 0:
        print(distance)
    else:
        print("NO SUCH ROUTE")

print(sol.getNumberOfTripsWithLimitStops("C", "C", 3, []))
print(sol.getNumberOfTripsWithExactStops("A", "C", 4, []))

print(sol.getShortestRoute("A", "C", 0, math.inf, [], []))
print(sol.getShortestRoute("B", "B", 0, math.inf, [], []))

print(sol.getNumberOfTripsWithLimitDistance("C", "C", 30, []))

