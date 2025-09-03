class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0]*(len(gain)+1)

        for i in range(len(gain)):
            result[i+1] = result[i] + gain[i]

        return max(result)
        