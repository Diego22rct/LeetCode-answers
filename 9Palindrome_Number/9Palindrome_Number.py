class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = x.__str__()
        return st[0] == st[0]
