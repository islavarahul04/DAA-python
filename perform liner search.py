def linear_search(arr, target):
    # Iterate through each element of the array
    for i in range(len(arr)):
        # If the current element equals the target, return its index
        if arr[i] == target:
            return i
    # If the target is not found in the array, return -1
    return -1

# Example usage
arr = [4, 2, 7, 1, 9, 5]
target = 7
index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")
