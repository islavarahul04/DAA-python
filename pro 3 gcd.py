def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def gcd_factorization(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    
    common_factors = set(factors_a) & set(factors_b)
    gcd = 1
    for factor in common_factors:
        gcd *= factor

    return gcd

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate GCD using recursive factorization method
gcd_recursive_factorization = gcd_factorization(num1, num2)

print("GCD of", num1, "and", num2, "using recursive factorization is:", gcd_recursive_factorization)
