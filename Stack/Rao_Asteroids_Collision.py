class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        
        res = []
        for asteroid in asteroids:
            while res and asteroid < 0 and res[-1] > 0:
                top = res[-1]
                if abs(asteroid) > top:
                    res.pop()
                elif abs(asteroid) == top:
                    res.pop()
                    asteroid = 0
                    break
                else: #abs(asteroid) is < top
                    asteroid = 0
                    break
            if asteroid != 0:
                res.append(asteroid)
        return res