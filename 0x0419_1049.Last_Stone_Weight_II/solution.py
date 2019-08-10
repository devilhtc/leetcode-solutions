# knapsack solution by @yerbola
class Solution:
    def lastStoneWeightII(self, stones):
        def maximize(i, space_left):
            if (i, space_left) in memory:
                return memory[i, space_left]
            elif i == len(stones) or space_left == 0:
                return 0
            elif space_left < stones[i]:
                return maximize(i + 1, space_left)
            else:
                take_stone_i = stones[i] + maximize(i + 1, space_left - stones[i])
                not_take_stone_i = maximize(i + 1, space_left)
                max_sum_i = max(take_stone_i, not_take_stone_i)
                memory[i, space_left] = max_sum_i
                return max_sum_i

        memory = {}
        # Fill up the knapsack of size floor(sum(stones)/2) as fully as possible
        max_sum = maximize(0, sum(stones) / 2)
        return sum(stones) - 2 * max_sum
