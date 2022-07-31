class JewelStone:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value


class Solution:
    def assign(self, stones: [JewelStone], capacity: int):
        self.stones = stones
        self.capacity = capacity
        self.memory = [[-1]*(capacity+1) for i in range(len(stones))]

    def rcrsv(self, position: int, capacity: int):
        if capacity <= 0:
            return 0
        if position < 0:
            return 0
        if self.memory[position][capacity] != -1:
            return self.memory[position][capacity]
        if position == 0:
            if capacity >= self.stones[position].weight:
                result = self.stones[position].value
                self.memory[position][capacity] = result
                return result
            else:
                self.memory[position][capacity] = 0
                return 0
        if capacity - self.stones[position].weight < 0:
            result = self.rcrsv(position - 1, capacity)
            self.memory[position][capacity] = result
            return result

        result = max(self.rcrsv(position - 1, capacity - self.stones[position].weight) +
                     self.stones[position].value,
                     self.rcrsv(position - 1, capacity))
        self.memory[position][capacity] = result
        return result

    def getMaxValue(self, stones: [JewelStone], capacity: int) -> int:
        self.assign(stones, capacity)
        position = len(stones) - 1
        return self.rcrsv(position, capacity)


li = [(1, 3), (2, 4), (3, 5), (4, 7)]
stones = []

for i in li:
    stones.append(JewelStone(weight=i[0], value=i[1]))


solution = Solution()
print(solution.getMaxValue(stones, 5))
