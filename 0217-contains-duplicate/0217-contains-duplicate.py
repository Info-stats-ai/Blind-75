class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hset = set()
        for key , value in enumerate(nums) :
            if value in hset:
                return True
            hset.add(value)
        return False


    
    