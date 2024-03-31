import itertools

def tsp_dp(distances):
    n = len(distances)
    # Initialize the memoization table
    memo = {}

    # Recursive function to calculate the shortest path
    def tsp_dp_helper(curr, visited):
        # Base case: if all cities have been visited, return the distance to the starting city
        if len(visited) == n:
            return distances[curr][0]

        # If the subproblem has already been solved, return the memoized value
        if (curr, tuple(visited)) in memo:
            return memo[(curr, tuple(visited))]

        # Try all unvisited cities as the next destination
        min_distance = float('inf')
        for next_city in range(n):
            if next_city not in visited:
                new_visited = visited + [next_city]
                distance = distances[curr][next_city] + tsp_dp_helper(next_city, new_visited)
                min_distance = min(min_distance, distance)

        # Memoize the result
        memo[(curr, tuple(visited))] = min_distance
        return min_distance

    # Start the recursive search from city 0
    return tsp_dp_helper(0, [0])

# Example usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_distance = tsp_dp(distances)
print("Shortest distance:", shortest_distance)
