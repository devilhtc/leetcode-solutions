class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        l = len(position)
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(l)]
        cars = sorted(cars)
        stack = []
        for i in range(l):
            s, t = cars[i]
            while len(stack) > 0 and stack[-1][1] <= t:
                stack.pop()
            stack.append((s, t))
        return len(stack)
