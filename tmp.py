class NumArray:
    def __init__(self, nums: List[int]):
        self.cache = [0]*len(nums)
        sm=0
        for i in range(len(nums)):
            sm += nums[i]
            self.cache[i] = sm

    def sumRange(self, i: int, j: int) -> int:
        if i!=0:
            return self.cache[j]-self.cache[i-1]
        else:
            return self.cache[j]

spis = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

print(["NumArray", "sumRange", "sumRange", "sumRange"])