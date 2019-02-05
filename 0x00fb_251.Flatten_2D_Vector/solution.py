class Vector2D:
    def __init__(self, v: "List[List[int]]"):
        self.stack = [[v, 0]]
        self.findNext()

    def next(self) -> "int":
        a, b = self.stack[-1]
        out = a[b]
        self.stack[-1][1] += 1
        self.findNext()
        return out

    def hasNext(self) -> "bool":
        return len(self.stack) > 0

    def findNext(self):
        while len(self.stack) > 0:
            a, b = self.stack[-1]
            if b == len(a):
                self.stack.pop()
                if len(self.stack) > 0:
                    self.stack[-1][1] += 1
                continue
            else:
                if isinstance(a[b], int):
                    break
                else:
                    self.stack.append([a[b], 0])


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
