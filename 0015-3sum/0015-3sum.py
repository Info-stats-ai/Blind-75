class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo = i + 1
            hi = len(nums) - 1

            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if total == 0:
                    result.append([nums[i], nums[lo], nums[hi]])

                    # skip duplicates for lo and hi
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1

                    lo += 1
                    hi -= 1

                elif total < 0:
                    lo += 1    # sum too small, move lo right
                else:
                    hi -= 1    # sum too big, move hi left

        return result