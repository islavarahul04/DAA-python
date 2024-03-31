def is_perfect_number(n):
    # Check if n is less than 2
    if n < 2:
        return False
    
    # Find the sum of proper divisors
    divisor_sum = 1  # 1 is always a divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting square root twice
                divisor_sum += n // i
    
    # Check if the sum of proper divisors equals n
    return divisor_sum == n

# Example usage
for number in range(2, 10000):
    if is_perfect_number(number):
        print(number, "is a perfect number.")
