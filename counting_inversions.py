def sort_count(arr):
    """
    Numerical similarity measure between two ranked lists through counting the
    number of inversions. Used for collaborative filtering (finding similar
    users to a certain user)

    Returns:
        int: count of pairs of indexes, i, j in the array for which i < j and
        arr[i] > arr[j]
    """
    def merge_count(left, right):
        merged = []
        count = 0

        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                count += len(left)
                merged.append(right.pop(0))

        if left:
            merged.extend(left)
        else:
            merged.extend(right)

        return merged, count

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) >> 1

    left, left_count = sort_count(arr[:mid])
    right, right_count = sort_count(arr[mid:])
    split, split_count = merge_count(left, right)

    count = left_count + right_count + split_count

    return split, count

print sort_count([1, 2])