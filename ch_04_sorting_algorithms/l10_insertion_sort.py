# Better than merge sort in time, in a case where the list is mostly sorted
# much better than merge sort in memory, due to sort in place instead of recursive copies
def insertion_sort(nums):
    i, j = 1, 1
    while i < len(nums):
        j = i
        while j > 0 and (nums[j - 1] > nums[j]):
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        i += 1
    return nums
