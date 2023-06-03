def merge_sort(arr, left, right):
    if right > left:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    temp_arr = []
    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            temp_arr.append(arr[j])
            j += 1
        else:
            temp_arr.append(arr[i])
            i += 1

    while i <= mid:
        temp_arr.append(arr[i])
        i += 1

    while j <= right:
        temp_arr.append(arr[j])
        j += 1

    for P in range(left, right + 1):
        arr[P] = temp_arr[P - left]

arr = [10, 8, 15, 9, 7, 11]
left = 0
right = len(arr) - 1
merge_sort(arr, left, right)
print(arr)
