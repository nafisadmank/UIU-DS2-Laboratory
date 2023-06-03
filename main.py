def merge_sort(arr, left, right):
    inv_count = 0  # Initialize the inversion count
    if right > left:
        mid = (left + right) // 2  # Calculate the middle index
        inv_count += merge_sort(arr, left, mid)  # Recursively sort the left half and update inversion count
        inv_count += merge_sort(arr, mid + 1, right)  # Recursively sort the right half and update inversion count
        inv_count += merge(arr, left, mid, right)  # Merge the sorted halves and update inversion count
    return inv_count  # Return the total inversion count

def merge(arr, left, mid, right):
    i = left  # Index for the left subarray
    j = mid + 1  # Index for the right subarray
    temp_arr = []  # Temporary array to store merged elements
    inv_count = 0  # Initialize the inversion count for this merge operation
    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            temp_arr.append(arr[j])  # Append the smaller element from the right subarray
            j += 1
            inv_count += (mid - i + 1)  # Increment inversion count by the number of remaining elements in the left subarray
        else:
            temp_arr.append(arr[i])  # Append the smaller element from the left subarray
            i += 1

    while i <= mid:
        temp_arr.append(arr[i])  # Append any remaining elements from the left subarray
        i += 1

    while j <= right:
        temp_arr.append(arr[j])  # Append any remaining elements from the right subarray
        j += 1

    for P in range(left, right + 1):
        arr[P] = temp_arr[P - left]  # Copy the sorted elements back to the original array

    return inv_count  # Return the inversion count for this merge operation

arr = [10, 8, 15, 9, 7, 11]
left = 0
right = len(arr) - 1
print("Number of inversions:", merge_sort(arr, left, right))  # Print the total number of inversions
print("Sorted array:", arr)  # Print the sorted array
