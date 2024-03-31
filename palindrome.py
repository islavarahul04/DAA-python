def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase for case-insensitive comparison
    if len(s) <= 1:  # Base case: if the length of the string is 0 or 1, it's a palindrome
        return True
    elif s[0] != s[-1]:  # If the first and last characters are not equal, it's not a palindrome
        return False
    else:
        # Recursively check if the substring excluding the first and last characters is a palindrome
        return is_palindrome(s[1:-1])

# Input string from the user
string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
