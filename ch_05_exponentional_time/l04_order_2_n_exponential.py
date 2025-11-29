def power_set(input):
    if not input:
        return [[]]
    all_subsets = [[]]
    for i in input:
        new_subsets = []
        for subset in all_subsets:
            new_subset = subset + [i]
            new_subsets.append(new_subset)
            # print(f"subset: {subset}")
            # print(f"i: {i}")
            # print(f"new_subset: {new_subset}")
        all_subsets.extend(new_subsets)
    return all_subsets
