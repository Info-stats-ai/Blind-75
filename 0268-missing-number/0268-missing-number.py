class Solution:
    def missingNumber(self, nums: list[int]) -> int:
         Maximum = len(nums)
         total = (Maximum*(Maximum +1))/ 2
         summation = 0
         for i in range(len(nums)):
            summation = summation + nums[i]
         return  int(total - summation)

        
