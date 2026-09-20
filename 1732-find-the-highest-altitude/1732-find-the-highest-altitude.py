class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        result = [0]
        temp = 0
        for i in gain:
            temp+=i
            result.append(temp)
        return max(result)