dijs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
d2idx = {"U": 0, "L": 1, "R": 2, "D": 3}


class SnakeGame:
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.score = 0
        self.snake = collections.deque([(0, 0)])
        self.snakeset = set([(0, 0)])
        self.food = food

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        di, dj = dijs[d2idx[direction]]
        hi, hj = self.snake[0]
        ni, nj = hi + di, hj + dj
        if not (0 <= ni <= self.height - 1 and 0 <= nj <= self.width - 1):
            return -1  # out of boudary
        if self.score < len(self.food) and tuple(self.food[self.score]) == (
            ni,
            nj,
        ):  # eat
            self.snake.appendleft((ni, nj))
            self.snakeset.add((ni, nj))
            self.score += 1
            return self.score
        else:
            ti, tj = self.snake.pop()
            self.snakeset.remove((ti, tj))
            if (ni, nj) in self.snakeset:
                return -1  # collide
            self.snake.appendleft((ni, nj))
            self.snakeset.add((ni, nj))
            return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
