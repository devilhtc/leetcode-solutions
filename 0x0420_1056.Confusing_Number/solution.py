class Solution:
    def confusingNumber(self, N: int) -> bool:
        digits = []
        d = {0: 0, 1: 1, 6: 9, 8: 0, 9: 6}
        while N > 0:
            N, r = divmod(N, 10)
            if r not in d:
                return False
            digits.append(r)
        i = 0
        j = len(digits) - 1
        while i <= j:
            if d[digits[i]] != digits[j]:
                return True
            i += 1
            j -= 1
        return False
