def generate_pattern(n):
    if n == 1:
        print("1")
        return

    generate_pattern(n - 1)

    line = ""
    for i in range(n):
        line += str(n) + " "
    print(line)

# Example usage
generate_pattern(5)
