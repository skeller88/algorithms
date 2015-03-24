def quicksort(arr):
    def swap(arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def partition(arr, left, right):
        pivot = (left + right) >> 1
        pivot_el = arr[pivot]
        lo = left

        swap(arr, right, pivot)

        for ind in xrange(left, right):
            if arr[ind] <= arr[right]:
                swap(arr, ind, lo)
                lo += 1

        swap(arr, lo, right)
        return lo

    def _quicksort(arr, left, right):
        if left < right:
            p = partition(arr, left, right)
            _quicksort(arr, left, p - 1)
            _quicksort(arr, p + 1, right)

    _quicksort(arr, 0, len(arr) - 1)

a = [1,7,-1,99,8,4]
quicksort(a)
print a
