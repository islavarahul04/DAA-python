def is_prime(n, divisor=2):
    """
    Checks if a number is prime recursively.
    
    Parameters:
        n (int): The number to check for primality.
        divisor (int): The current divisor being tested.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Base cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    
    # Recursive case
    return is_prime(n, divisor + 1)

def generate_primes(start, end):
    """
    Generates all prime numbers in the given range using recursion.
    
    Parameters:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        
    Returns:
        list: A list of prime numbers in the given range.
    """
    if start > end:
        return []
    
    primes = []
    if is_prime(start):
        primes.append(start)
    primes += generate_primes(start + 1, end)
    
    return primes

# Test the function
start_num = 1
end_num = 50
print(f"Prime numbers between {start_num} and {end_num}:")
print(generate_primes(start_num, end_num))
