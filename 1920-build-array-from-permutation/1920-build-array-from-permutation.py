class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = nums.copy()
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
            
