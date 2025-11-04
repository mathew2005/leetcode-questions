class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same length
        # sort both s and t, check if s == t
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        return s == t
        
        # T: O(nlogn + nlogn)
        # S:O(1)