class Solution:
    def findMin(self, nums: List[int]) -> int:

        

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
            # The drop/pivot is in the right half
                l = mid + 1
            else:
            # The minimum is in the left half, including mid
                r = mid

        return nums[l]