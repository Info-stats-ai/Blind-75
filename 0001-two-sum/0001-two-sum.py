class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmaps = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in hashmaps:
                return [hashmaps[diff], i]
            hashmaps[x] = i
        return
    