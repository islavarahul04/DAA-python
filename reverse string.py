def reverse_string(string):
    """
    Recursively prints the reverse of a string.
    
    Parameters:
        string (str): The string to be reversed.
    """
    # Base case: If the string is empty, return
    if len(string) == 0:
        return
    
    # Print the last character of the string
    print(string[-1], end="")
    
    # Recursive call to print the reverse of the substring excluding the last character
    reverse_string(string[:-1])

# Test the function
input_string = "Hello, World!"
print("Original String:", input_string)
print("Reversed String:", end=" ")
reverse_string(input_string)
