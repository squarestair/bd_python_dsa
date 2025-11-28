def merge_sort(nums):
    if len(nums) < 2:
        return nums
    half = len(nums) // 2
    first = nums[:half]
    second = nums[half:]
    # print(first, " and ", second)
    sorted_left = merge_sort(first)
    sorted_right = merge_sort(second)
    return merge(sorted_left, sorted_right)


def merge(first, second):
    final = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        # print(first, " and ", second)
        # print(f"first i == {first[i]} second j == {second[j]}")
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
            # print("final append first:", final)
        else:
            final.append(second[j])
            j += 1
            # print("final append second:", final)

    while i < len(first) or j < len(second):
        if i < len(first):
            final.append(first[i])
            i += 1
            # print("final: append first", final)
        else:
            final.append(second[j])
            j += 1
            # print("final: append second", final)
    return final
