def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.
    
    Parameters:
        arr (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    
    Parameters:
        left (list): The left sorted list.
        right (list): The right sorted list.
        
    Returns:
        list: The merged sorted list.
    """
    result = []
    left_index = right_index = 0
    
    # Merge the left and right lists into the result list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements from the left and right lists
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Test the function
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
