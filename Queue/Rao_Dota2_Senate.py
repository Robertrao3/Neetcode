class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if not senate:
            return ""
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, senator_party in enumerate(senate):
            if senator_party == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            radiantindex = radiant.popleft()
            direindex = dire.popleft()

            if radiantindex < direindex:
                radiant.append(radiantindex + n)
            else:
                dire.append(direindex + n)
        
        if radiant:
            return "Radiant"
        else:
            return "Dire"
