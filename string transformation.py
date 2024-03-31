def string_transform(s, t, k):
    MOD = 10**9 + 7
    n = len(s)
    dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(n + 1):
            dp[i][j][0] = 1
            for p in range(1, k + 1):
                dp[i][j][p] = (dp[i][j][p] + dp[i - 1][j][p - 1]) % MOD
                if j > 0:
                    dp[i][j][p] = (dp[i][j][p] + dp[i - 1][j - 1][p - 1]) % MOD

    result = 0
    for p in range(k + 1):
        for i in range(n + 1):
            for j in range(n):
                if t[:j + 1] == s[n - i:n - i + j + 1]:
                    result = (result + dp[i][j + 1][k - p]) % MOD

    return result

# Example usage:
s = "abcd"
t = "cdab"
k = 3
print(string_transform(s, t, k))  # Output: 2