class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        result = []

        current = intervals[0] # [1,6]
        
        for next_interval in intervals[1:]:
            if next_interval[0] <= current[1]:
                current[1] = max(current[1], next_interval[1])

            else:
                result.append(current)
                current = next_interval

        result.append(current)

        return result

        