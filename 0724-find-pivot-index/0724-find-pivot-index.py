# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:

#         for pivot in range(len(nums)):
#             if sum(nums[:pivot]) == sum(nums[pivot+1:]):
#                 return pivot
#         return -1 # 루프 다 돈 다음에 업으면 return -1 해야지.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i,x in enumerate(nums):
            right = total - left - x
            if left == right :
                return i
            left +=x #왼쪽 합 누적 필요
        return -1

        