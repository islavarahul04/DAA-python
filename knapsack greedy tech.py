def fractional_knapsack(weights, values, capacity):
    """
    Solves the Knapsack problem using the Fractional Knapsack algorithm.
    
    Parameters:
        weights (list): List of weights of items.
        values (list): List of values of items.
        capacity (float): Maximum capacity of the knapsack.
        
    Returns:
        float: Maximum value that can be achieved.
    """
    # Calculate value-to-weight ratio for each item
    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    
    # Sort items by value-to-weight ratio in descending order
    value_per_weight.sort(reverse=True)
    
    max_value = 0
    
    for ratio, weight, value in value_per_weight:
        if capacity >= weight:
            # Take the whole item
            max_value += value
            capacity -= weight
        else:
            # Take a fraction of the item
            max_value += (capacity / weight) * value
            break
    
    return max_value

# Test the function
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be achieved:", max_value)
