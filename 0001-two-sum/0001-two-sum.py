class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for key, value in enumerate(nums):
            diff = target - value 
            if diff in hashmap:
                return [hashmap[diff], key]
            else:
                hashmap[value] = key
        return
        