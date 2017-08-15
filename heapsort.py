# build the heap
# take the max element out of the heap, and repair

def swap(sqc, i, j):
    sqc[i], sqc[j] = sqc[j], sqc[i]

def heapify(arr, end, parent):
  left = parent * 2 + 1
  right = parent * 2 + 2
  max = parent

  if left < end and arr[left] > arr[parent]:
    max = left

  if right < end and arr[right] > arr[parent]:
    max = right

  if max != parent:
    swap(arr, parent, max)
    heapify(arr, end, max)

def heap_sort(arr):
  end = len(arr)
  start_parent = end // 2 - 1

  # build the heap
  for parent in xrange(start_parent, -1, -1):
    heapify(arr, end, parent)

  for ind in xrange(end - 1, 0, -1):
    swap(arr, ind, 0)
    heapify(arr, ind, 0)

  return arr

print heap_sort([5,1,7,3,3])