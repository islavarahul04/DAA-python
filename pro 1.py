def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(count):
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(count):
            print(fibonacci(i), end=" ")

# Example usage
count = 15  # Change the count as per your requirement
print_fibonacci_series(count)
