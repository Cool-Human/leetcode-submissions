class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def helper(res):
            ans = []
            
            for asteroid in res:
                if not ans:
                    ans.append(asteroid)
                elif ans[-1] * asteroid > 0 or (ans[-1] < 0 and asteroid > 0):
                    ans.append(asteroid)
                else:
                    if abs(ans[-1]) == abs(asteroid):
                        ans.pop()
                    elif abs(ans[-1]) > abs(asteroid):
                        continue
                    else:
                        ans.pop()
                        ans.append(asteroid)
            
            if len(ans) == len(res):
                return res
            else:
                return helper(ans)

        return helper(asteroids)