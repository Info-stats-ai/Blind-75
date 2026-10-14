class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxP = nums[0]
        currMin = 1
        currMax = 1 
        for i in range(len(nums)):
            tmp = currMax
            currMax = max(currMax*nums[i], currMin*nums[i], nums[i])
            currMin = min(tmp*nums[i], currMin*nums[i], nums[i])
            maxP = max(maxP, currMax)
        return maxP
                
                


         

        