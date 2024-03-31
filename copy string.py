def copy_string(source, destination, index=0):
    """
    Recursively copies characters from source string to destination string.
    
    Parameters:
        source (str): The source string to be copied.
        destination (str): The destination string where characters will be copied to.
        index (int): The current index being processed.
    
    Returns:
        str: The destination string after copying.
    """
    # Base case: If index exceeds the length of source string, return destination string
    if index == len(source):
        return destination
    
    # Copy the character at current index from source to destination
    destination += source[index]
    
    # Recursive call to copy next character
    return copy_string(source, destination, index + 1)

# Test the function
source_str = "Hello, World!"
destination_str = ""
destination_str = copy_string(source_str, destination_str)
print("Source String:", source_str)
print("Destination String:", destination_str)
