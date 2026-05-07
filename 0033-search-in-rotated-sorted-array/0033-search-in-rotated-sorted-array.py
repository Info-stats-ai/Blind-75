class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:  # target in left half
                    hi = mid - 1
                else:
                    lo = mid + 1                     # target in right half

            # right half is sorted
            else:
                if nums[mid] < target <= nums[hi]:  # target in right half
                    lo = mid + 1
                else:
                    hi = mid - 1                     # target in left half

        return -1    # exhausted search, not found