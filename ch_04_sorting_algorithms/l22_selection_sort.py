def selection_sort(nums):
    for i in range(len(nums)):
        sm_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[sm_idx]:
                sm_idx = j
        nums[i], nums[sm_idx] = nums[sm_idx], nums[i]
    return nums
