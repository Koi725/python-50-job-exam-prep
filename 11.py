def calculate_odd_sum(start, end):
    """
    Calculates the sum of all ODD numbers between two integers (inclusive).
    Automatically handles the order of inputs.
    """
    lower = min(start, end)
    upper = max(start, end)

    total = 0
    for number in range(lower, upper + 1):
        if number % 2 != 0:
            total += number

    return total


def main():
    print("🔢 Welcome to the ODD Number Sum Calculator 🔢\n")

    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.\n")
            continue

        result = calculate_odd_sum(num1, num2)
        print(f"\nThe sum of ODD numbers between {num1} and {num2} is: {result}")
        print("-" * 50)

        again = input("Would you like to try again? (y/n): ").strip().lower()
        if again != "y":
            print("\nExiting the program. See you next time!")
            break

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
