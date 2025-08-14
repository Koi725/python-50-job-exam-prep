"""
Q04 — Sum of squares of three numbers

Write a program that takes three numbers as input, finds the sum of their squares,
and prints "YES" if the result is greater than 20, otherwise prints "NO".
"""


def calc_sum_of_squares(num1: float, num2: float, num3: float) -> None:
    """Calculate the sum of squares of three numbers and print YES/NO."""
    sum_squares = num1**2 + num2**2 + num3**2
    if sum_squares > 20:
        print("YES")
    else:
        print("NO")


def main() -> None:
    """Collect three numbers from the user and run the calculation."""
    numbers = []
    for i in range(1, 4):
        while True:
            try:
                user_input = float(input(f"Please enter number {i}: "))
                numbers.append(user_input)
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
    calc_sum_of_squares(*numbers)


if __name__ == "__main__":
    main()
