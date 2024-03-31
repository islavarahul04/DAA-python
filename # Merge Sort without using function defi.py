# Merge Sort without using function definitions

# Merge two sorted sublists arr[l..m] and arr[m+1..r]
def merge(arr, l, m, r):
    i, j, k = l, m + 1, 0
    temp = [0] * (r - l + 1)

    # Merge the two halves into temp[]
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= m:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged elements into original list arr[]
    for i in range(l, r + 1):
        arr[i] = temp[i - l]

# Main function to sort an array using merge sort
def mergeSort(arr):
    n = len(arr)
    curr_size = 1

    # Iterate over subarray size, then merge subarrays of that size
    while curr_size < n - 1:
        left = 0

        # Pick starting point of different subarrays of current size
        while left < n - 1:
            mid = left + curr_size - 1

            # Find ending point of left subarray
            right = min((left + 2 * curr_size - 1), (n - 1))

            # Merge subarrays arr[left...mid] & arr[mid+1...right]
            merge(arr, left, mid, right)
            left += 2 * curr_size

        curr_size *= 2

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)

mergeSort(arr)

print("Sorted array is", arr)
