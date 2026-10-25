class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.pop(stones.index(max1))
            max2 = max(stones)
            stones.pop(stones.index(max2))
            if max1 != max2 :
                stones.append(max1-max2)
        if len(stones) > 0 :
            return stones[0]
        else:
            return 0

        