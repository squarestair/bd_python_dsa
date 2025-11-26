def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        i = 1
        while i < end:
            # If previous (left) element is greater than next (right) element, swap
            if (nums[i - 1]) > nums[i]:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                swapping = True
            i += 1
        end -= 1
    return nums
