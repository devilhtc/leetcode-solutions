class Solution:
    def asteroidCollision(self, asteroids: "List[int]") -> "List[int]":
        stack = []
        for ele in asteroids:
            if len(stack) == 0 or ele > 0:
                stack.append(ele)
                continue
            else:
                d = False
                while len(stack) > 0:
                    last = stack[-1]
                    if last < 0:
                        break
                    else:  # collide
                        if last > -ele:
                            d = True
                            break
                        elif last == -ele:
                            d = True
                            stack.pop()
                            break
                        else:
                            stack.pop()
                if not d:
                    stack.append(ele)
        return stack
