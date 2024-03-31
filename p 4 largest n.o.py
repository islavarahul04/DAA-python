def find_largest_element(arr):
    if not arr:
        return None  # If the array is empty, return None
    
    max_element = arr[0]  # Initialize max_element to the first element of the array
    
    # Iterate through the array to find the maximum element
    for element in arr:
        if element > max_element:
            max_element = element
    
    return max_element

# Example usage:
array = [10, 5, 20, 8, 15]
largest_element = find_largest_element(array)
print("The largest element in the array is:", largest_element)
