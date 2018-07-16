# binary index tree


class BIT1D(object):
    def __init__(self, arr):
        self.arr = arr
        self.bit = [0] * (len(arr) + 1)
        self.maxlen = len(arr)

        # update the index_th element

    def update(self, index, val):
        if index <= 0 or index > self.maxlen:
            return
        x = index
        self.arr[x - 1] += val
        while x <= self.maxlen:
            self.bit[x] += val
            x += x & -x

            # how many elements

    def query(self, index):
        if index < 0 or index > self.maxlen:
            return 0
        x = index
        out = 0
        while x > 0:
            out += self.bit[x]
            x -= x & -x

        return out

    def rangeQuery(self, start, end):
        return self.query(end) - self.query(start - 1)

    def build(self):
        for i, num in enumerate(self.arr):
            self.update(i + 1, num)


class BIT2D(object):
    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.bit = [[0 for x in range(len(grid[0]) + 1)] for y in range(len(grid) + 1)]

        # update the index_th element

    def update(self, i, j, val):
        if i <= 0 or i > self.m:
            return
        if j <= 0 or j > self.n:
            return
        x = i

        self.grid[i - 1][j - 1] += val
        while x <= self.m:
            y = j
            while y <= self.n:
                self.bit[x][y] += val
                y += y & -y
            x += x & -x

            # how many elements

    def query(self, i, j):
        if i < 0 or i > self.m:
            return 0
        if j < 0 or j > self.n:
            return 0
        x = i
        out = 0
        while x > 0:
            y = j
            while y > 0:
                out += self.bit[x][y]
                y -= y & -y
            x -= x & -x
        return out

    def rangeQuery(self, i1, j1, i2, j2):
        return (
            self.query(i1 - 1, j1 - 1)
            - self.query(i1 - 1, j2)
            - self.query(i2, j1 - 1)
            + self.query(i2, j2)
        )

    def build(self):
        for i, nums in enumerate(self.grid):
            for j, num in enumerate(nums):
                self.update(i + 1, j + 1, num)


def bit2trial():
    bit2 = BIT2D([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    bit2.build()
    bit2.update(4, 3, 2)


def bit1trial():
    bit1 = BIT1D([1, 2, 3, 4, 5])
    bit1.build()
    bit1.update(5, 2)


def main():
    bit2trial()


if __name__ == "__main__":
    main()
