def make_sum_in_range(num1, num2):
    """
    Custom implementation to calculate the sum of integers
    between two numbers (inclusive), using a for loop.
    """
    lower = min(num1, num2)
    upper = max(num1, num2)

    total = 0
    for i in range(lower, upper + 1):
        total += i  # step-by-step accumulation

    return total


def main():
    print("🔢 Welcome to the Range Sum Calculator!")

    while True:
        try:
            num1 = int(input(" Enter the first number: "))
            num2 = int(input(" Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.\n")
            continue

        total = make_sum_in_range(num1, num2)
        print(f"The sum from {min(num1, num2)} to {max(num1, num2)} is: {total}\n")

        query = input(" Do you want to continue? (y/n): ").strip().lower()
        if query != "y":
            print(" Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
