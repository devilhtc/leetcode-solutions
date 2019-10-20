class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l = math.gcd(len(str1), len(str2))
        s = str1[:l]
        for i, c in enumerate(str1):
            if c != s[i % l]:
                return ""
        for i, c in enumerate(str2):
            if c != s[i % l]:
                return ""
        return s
