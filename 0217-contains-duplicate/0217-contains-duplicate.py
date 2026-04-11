class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for k, v in enumerate(nums):
            if v in hashmap :
                return True
            hashmap[v] = k
        return False
        