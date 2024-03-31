def container_loader(items, container_capacity):
    containers = [[]]

    for item in sorted(items, reverse=True):
        for container in containers:
            if sum(container) + item <= container_capacity:
                container.append(item)
                break
        else:
            containers.append([item])

    return containers

# Example usage
items = [3, 2, 5, 4, 7, 6, 8]
container_capacity = 10
result = container_loader(items, container_capacity)
print("Containers:")
for i, container in enumerate(result, 1):
    print(f"Container {i}: {container}")
