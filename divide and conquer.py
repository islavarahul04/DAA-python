def find_max_min(arr, left, right):
    """
    Finds both the maximum and minimum values in a list using Divide and Conquer.
    
    Parameters:
        arr (list): The list of numbers.
        left (int): The left index of the sublist.
        right (int): The right index of the sublist.
        
    Returns:
        tuple: A tuple containing the maximum and minimum values.
    """
    # Base case: If sublist has only one element
    if left == right:
        return (arr[left], arr[left])
    
    # If sublist has two elements, compare and return
    if right - left == 1:
        return (max(arr[left], arr[right]), min(arr[left], arr[right]))
    
    # Divide the sublist into two halves
    mid = (left + right) // 2
    max_left, min_left = find_max_min(arr, left, mid)
    max_right, min_right = find_max_min(arr, mid + 1, right)
    
    # Combine results from both halves
    return (max(max_left, max_right), min(min_left, min_right))

# Test the function
arr = [3, 7, 2, 8, 9, 1, 4, 6]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Original list:", arr)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
