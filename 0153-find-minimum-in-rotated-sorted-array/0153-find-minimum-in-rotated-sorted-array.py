class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:        # not lo <= hi, we want a single element left
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1  # min is in right half
            else:
                hi = mid      # min is in left half (mid could be the answer)

        return nums[lo]       # lo == hi, we found the minimum
