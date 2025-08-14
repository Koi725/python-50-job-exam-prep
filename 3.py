"""
Q03 — Print the larger of two numbers

Write a program that takes two numbers as input and prints the larger number.
If both numbers are equal, print a message stating they are equal.
"""


def print_larger_number(num1: float, num2: float) -> None:
    """Print which number is larger, or if they are equal."""
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"Both numbers are equal: {num1}")


def main() -> None:
    """Main function to collect inputs and display the larger number."""
    numbers = []
    for i in range(1, 3):
        while True:
            try:
                user_input = float(input(f"Please enter number {i}: "))
                numbers.append(user_input)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    print_larger_number(*numbers)


if __name__ == "__main__":
    main()
