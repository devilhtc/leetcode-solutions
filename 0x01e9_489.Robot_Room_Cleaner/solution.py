# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goto(pos1, pos2):
            # robot always face up
            if pos2[0] - pos1[0] == 1:
                # go right
                robot.turnRight()
                m = robot.move()
                robot.turnLeft()
            elif pos2[0] - pos1[0] == -1:
                # go left
                robot.turnLeft()
                m = robot.move()
                robot.turnRight()
            elif pos2[1] - pos1[1] == 1:
                # go up
                m = robot.move()
            else:
                # go down
                robot.turnLeft()
                robot.turnLeft()
                m = robot.move()
                robot.turnLeft()
                robot.turnLeft()
            return m

        visited = collections.defaultdict(lambda: False)
        x = 0
        y = 0
        stack = [[0, 0, 0]]
        visited[(0, 0)] = True
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while len(stack) > 0:
            last = stack[-1]
            x, y, t = tuple(last)
            if t == 4:
                robot.clean()
                stack.pop()
                if len(stack) > 0:
                    # backtrack
                    goto((x, y), stack[-1][:2])
                continue
            dx, dy = dirs[t]
            nx, ny = x + dx, y + dy
            stack[-1][2] += 1
            if visited[(nx, ny)]:
                continue
            m = goto((x, y), (nx, ny))
            if m: # moved to (nx, ny)
                visited[(nx, ny)] = True
                stack.append([nx, ny, 0])
    

