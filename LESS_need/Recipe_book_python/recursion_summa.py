def sum(nums):
    head, *tails = nums
    return head + sum(tails) if tails else head

if __name__ == '__main__':
    print(sum([4, 9, 10, 15, 3]))