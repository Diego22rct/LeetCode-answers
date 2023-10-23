from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        length = len(nums) - 1
        return [
            self.findLeft(nums, target, length),
            self.findRight(nums, target, length),
        ]

    def findLeft(self, nums, target, length):
        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    def findRight(self, nums, target, length):
        left, right = 0, length
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left if nums[left] == target else -1

    def find(self, nums, target, length):
        left, right = 0, length
        while left < right:
            mid = (left + right + 1) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return left if nums[left] == target else -1
