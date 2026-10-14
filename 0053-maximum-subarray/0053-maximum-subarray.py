class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        for i in range(len(nums)):
            
            if currsum < 0 :
                currsum = 0 
            currsum += nums[i]
            maxsum = max(maxsum, currsum)
        return maxsum




   

                
        