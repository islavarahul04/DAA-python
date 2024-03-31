def is_prime(n, divisor=2):
    if n <= 1:  # 1 and below are not prime numbers
        return False
    if n == divisor:  # Base case: n is only divisible by itself, so it's prime
        return True
    if n % divisor == 0:  # If n is divisible by any number other than 1 and itself, it's not prime
        return False
    else:
        return is_prime(n, divisor + 1)  # Recursive case: check divisibility with next divisor

# Input number from the user
num = int(input("Enter a positive integer: "))

# Check if the input is a prime number
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
