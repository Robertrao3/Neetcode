class Solution:
    def carFleet(self, target, positions, speed):
        time = [float(target - p) / s for p,s in sorted(zip(positions, speed))]
        res = current = 0

        for t in time[::-1]:
            if t > current:
                res += 1
                current = t
        return res