def find_factors(n, i=1, factors=[]):
    if i > n:
        return factors
    
    if n % i == 0:
        factors.append(i)
    
    return find_factors(n, i + 1, factors)

# Example usage
n = 20
factors = find_factors(n)
print("Factors of", n, ":", factors)
