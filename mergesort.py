def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merged_i = 0
    left_i = 0
    right_i = 0

    while left_i < len(left) and right_i < len(right):
      if left[left_i] < right[right_i]:
        arr[merged_i] = left[left_i]
        left_i += 1
      else:
        arr[merged_i] = right[right_i]
        right_i += 1
      merged_i += 1

    while left_i < len(left):
      arr[merged_i] = left[left_i]
      left_i += 1
      merged_i += 1

    while right_i < len(right):
      arr[merged_i] = right[right_i]
      right_i += 1
      merged_i += 1

arr = [5,2,1,7,5,8]
merge_sort(arr)
print arr