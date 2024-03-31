def optimal_bst(keys, freq):
    n = len(keys)
    # Create a table to store the costs of subtrees
    cost = [[0] * n for _ in range(n)]

    # Initialize the table for single keys
    for i in range(n):
        cost[i][i] = freq[i]

    # Calculate costs for chains of length 2 to n
    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            cost[i][j] = float('inf')
            total_freq = sum(freq[i:j + 1])

            # Try all keys as root and find minimum cost
            for k in range(i, j + 1):
                left_cost = cost[i][k - 1] if k > i else 0
                right_cost = cost[k + 1][j] if k < j else 0
                root_cost = total_freq + left_cost + right_cost
                if root_cost < cost[i][j]:
                    cost[i][j] = root_cost

    return cost[0][n - 1]

# Example usage
keys = [10, 12, 20]
freq = [34, 8, 50]
min_cost = optimal_bst(keys, freq)
print("Minimum cost of optimal binary search tree:", min_cost)
