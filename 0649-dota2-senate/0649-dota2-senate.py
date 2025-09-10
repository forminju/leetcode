class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        while True:
            if len(set(senate)) == 1:
                return "Dire" if senate[-1] =="D" else "Radiant"
            s = senate[0]
            senate = senate[1:]
            senate.append(s)
            if s =="D":
                senate.remove("R")
            else:
                senate.remove("D")
        