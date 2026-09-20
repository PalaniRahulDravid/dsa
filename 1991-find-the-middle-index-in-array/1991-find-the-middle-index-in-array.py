class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        l = 0
        for i in range(len(nums)):
            r = total-l-nums[i]
            if r==l:
                return i
            else:
                l+=nums[i]
        return -1