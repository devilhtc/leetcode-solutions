class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def helper(num):
            if num < 10:
                return 1 if d <= num else 0
            a, b = divmod(num, 10)
            cur_count = 0
            c = a
            while c > 0:
                c, e = divmod(c, 10)
                if e == d:
                    cur_count += 1
            return (
                cur_count * (b + 1)
                + (1 if b >= d else 0)
                + (helper(a - 1) - (1 if d == 0 else 0)) * 10
                + a
            )

        return helper(high) - helper(low - 1)
