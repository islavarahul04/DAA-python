def order(num):
    # Recursive function to find the order of the number
    if num == 0:
        return 0
    return 1 + order(num // 10)

def is_armstrong(num, n):
    # Recursive function to check if the number is an Armstrong number
    if num == 0:
        return 0
    return (num % 10)**n + is_armstrong(num // 10, n)

def check_armstrong(num):
    # Main function to check if the number is Armstrong
    n = order(num)
    armstrong_sum = is_armstrong(num, n)
    return armstrong_sum == num

# Example usage
number = int(input("Enter a number to check if it's an Armstrong number: "))
if check_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
