# Selection Sort without using function definitions

# Example usage of Selection Sort
arr = [64, 25, 12, 22, 11]

n = len(arr)

# Traverse through all elements in the list
for i in range(n):
    # Find the minimum element in the remaining unsorted list
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the found minimum element with the first element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Printing the sorted array
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
