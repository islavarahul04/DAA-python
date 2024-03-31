def subset_sum_helper(nums, target, current_sum, start, path, result):
    if current_sum == target:
        result.append(path[:])
        return
    
    for i in range(start, len(nums)):
        # If adding the current number doesn't exceed the target, proceed
        if current_sum + nums[i] <= target:
            # Include the current number in the path
            path.append(nums[i])
            # Recur with the updated sum and path
            subset_sum_helper(nums, target, current_sum + nums[i], i + 1, path, result)
            # Backtrack by removing the last added number
            path.pop()

def subset_sum(nums, target):
    result = []
    subset_sum_helper(nums, target, 0, 0, [], result)
    return result

# Example usage
nums = [2, 4, 6, 8]
target = 8
result = subset_sum(nums, target)
print("Subsets with sum equal to", target, "are:")
for subset in result:
    print(subset)
