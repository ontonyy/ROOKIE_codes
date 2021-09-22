def find_max(nums):
    max = 0
    for x in nums:
        if x > max:
            max = x
    return max

if __name__ == '__main__':
    print(find_max([2, 5, 7, 3, 12]))