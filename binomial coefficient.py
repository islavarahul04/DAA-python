def binomial_coefficient(n, k):
    # Initialize a table to store the binomial coefficients
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: C(n, 0) = C(n, n) = 1
    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][min(i, k)] = 1

    # Build the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

# Example usage
n = 5
k = 2
result = binomial_coefficient(n, k)
print(f"The binomial coefficient of {n} choose {k} is {result}")
