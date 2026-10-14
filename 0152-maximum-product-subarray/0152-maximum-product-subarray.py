class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums :
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax*n
            # created tmp for undated max
            curMax = max(n*curMin, n*curMax, n)#[-1, 8]
            curMin = min(tmp, n*curMin, n)#[-1, -8]
            res = max(res, curMax)
        return res


         

        