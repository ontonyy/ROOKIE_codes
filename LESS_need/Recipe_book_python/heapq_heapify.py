import heapq

nums = [3, -2, 9, 10, 15, 29, -1, -5, 7, 4]
heapq.heapify(nums)
print(nums)
while len(nums) != 0:
    heapq.heappop(nums)
    print(nums)

