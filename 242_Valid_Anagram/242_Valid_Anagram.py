from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter
