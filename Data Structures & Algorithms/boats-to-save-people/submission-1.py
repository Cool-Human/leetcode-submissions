class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        light, heavy = 0, len(people) - 1
        
        while light <= heavy:
            if people[heavy] + people[light] <= limit:
                res += 1
                heavy -= 1
                light += 1
            else:
                res += 1
                heavy -= 1
        
        return res