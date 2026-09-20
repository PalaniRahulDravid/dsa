class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        l = 0
        result = []
        for i in range(len(nums)):
            r = total - l -nums[i]
            diff = r-l
            if diff<0:
                result.append(-diff)
            else:
                result.append(diff)
            l+=nums[i]
        return result
        