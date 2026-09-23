class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        times = 2
        result = []

        for i in range(times):
            for n in nums:
                result.append(n)

        return result


        