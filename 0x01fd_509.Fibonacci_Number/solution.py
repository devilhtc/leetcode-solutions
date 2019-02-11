class Solution:
    def fib(self, N: "int") -> "int":
        if N <= 1:
            return N
        a, b = 1, 0
        for i in range(N - 1):
            a, b = a + b, a
        return a
