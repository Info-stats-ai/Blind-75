class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l ,r  = 0 ,len(numbers)- 1

        while l < r :
            s= numbers[l] + numbers[r]
            if target == s:
                return [l+1, r+1]
            elif target > s:
                l += 1
            else : 
                r -= 1
        

        