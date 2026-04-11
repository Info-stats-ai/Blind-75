class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for v in nums:
            if v in hashmap :
                return True
            hashmap[v] = True
        return False
        