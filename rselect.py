def r_select(arr, k):
    """
    Returns:
        int: maximum element if k > len(arr) and minimum element if k < 0
    """
    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def partition(start, end):
        pivot = (start + end) >> 1
        pivot_el = arr[pivot]
        lo = start

        swap(pivot, end)

        for ind in xrange(start, end):
            if arr[ind] <= pivot_el:
                swap(ind, lo)
                lo += 1

        swap(end, lo)

        return lo

    def _select(start, end, order_num):
        if start < end:
            p = partition(start, end)

            if p == k - 1:
                return arr[p]
            elif k > p:
                return _select(p + 1, end, order_num - p - 1)
            else:
                return _select(start, p - 1, order_num)

        return arr[start]

    return _select(0, len(arr) - 1, k)
