class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])

        result = []

        current = intervals[0]

        for next_int in intervals[1:]:
            if current[1] >= next_int[0]:
                current[1] = max(current[1], next_int[1])
            else:
                result.append(current)
                current = next_int

        result.append(current)

        return result
        