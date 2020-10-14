class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return self.recurse(locations, start, finish, fuel, { }) % (10**9 + 7)

    def recurse(self, locations, current, finish, fuel, cache):
        s = 0
        key = str(fuel) + " " + str(current)
        if key in cache:
            return cache[key]
        if fuel < 0: return s
        if fuel >= 0 and current == finish: 
            s += 1
        
        for i in range(len(locations)):
            if current == i: continue
            output = self.recurse(locations, i, finish, fuel - abs(locations[i] - locations[current]), cache)
            s += output
        cache[key] = s
        return s