class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minimum, maximum = max(weights), sum(weights)

        def finding_capacity(low, high):
            if low >= high:
                return low

            capacity = low + (high - low) // 2

            carrying = 0
            day = 1

            for weight in weights:
                if carrying + weight <= capacity:
                    carrying += weight
                else:
                    carrying = weight
                    day += 1

            if day <= days:
                return finding_capacity(low, capacity)
            else:
                return finding_capacity(capacity + 1, high)
        
        return finding_capacity(minimum, maximum)