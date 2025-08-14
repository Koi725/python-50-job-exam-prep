"""
Q07 — Smallest of three numbers

Write a program that takes three numbers as input and prints the smallest.
If all three are equal, print a special message.
"""


def smallest(num1: float, num2: float, num3: float) -> None:
    if num1 == num2 == num3:
        print(f"All three numbers are equal: {num1}")
    else:
        smallest_value = min(num1, num2, num3)
        print(f"The smallest number is: {smallest_value}")


def main() -> None:
    numbers = []
    for i in range(1, 4):
        while True:
            try:
                user_input = float(input(f"Please enter number {i}: "))
                numbers.append(user_input)
                break
            except ValueError:
                print("Invalid input! Please try again.")
    smallest(*numbers)


if __name__ == "__main__":
    main()
