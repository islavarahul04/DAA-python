def min_max_sequence(nums):
    """
    Prints the minimum and maximum value sequence for all the numbers in a list.
    
    Parameters:
        nums (list): A list of numbers.
    """
    if not nums:
        print("List is empty")
        return
    
    min_seq = nums[0]
    max_seq = nums[0]
    
    for num in nums[1:]:
        min_seq = min(num, min_seq + num)
        max_seq = max(num, max_seq + num)
        
    print("Minimum value sequence:", min_seq)
    print("Maximum value sequence:", max_seq)

# Test the function
numbers = [1, -3, 2, 1, -1]
print("Original List:", numbers)
min_max_sequence(numbers)
