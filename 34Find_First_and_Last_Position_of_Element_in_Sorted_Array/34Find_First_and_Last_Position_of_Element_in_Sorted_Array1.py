from typing import List


class Solution:
    def binary_search(self, list, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if list[mid] == x:
                return mid
            elif list[mid] > x:
                return self.binary_search(list, low, mid - 1, x)
            else:
                return self.binary_search(list, mid + 1, high, x)
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        length = len(nums) - 1

        return [
            self.binary_search(nums[: length // 2], 0, length, target),
            self.binary_search(nums[length // 2 :], 0, length, target),
        ]
