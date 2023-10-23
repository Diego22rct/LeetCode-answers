class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = []
        for num in nums:
            if num in hashset:
                return True
            hashset.append(num)
        return False
