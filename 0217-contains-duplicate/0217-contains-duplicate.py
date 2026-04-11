class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for v in nums:
            if v in hashmap :
                return True
            hashmap.add(v)
        return False
        