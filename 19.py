"""
Program: Triple Exponent Calculator (num1 ** num2 ** num3)
"""


def make_power(num1, num2, num3):
    """
    Returns: (num1 ** num2) ** num3
    """
    power = num1**num2
    result = power**num3
    return result


def main():
    print("=" * 50)
    print("🔢 Welcome to the Triple Power Calculator 🔢")
    print("This program calculates: (num1 ** num2) ** num3")
    print("=" * 50)

    while True:
        try:
            num1 = int(input("Enter the first number (base): "))
            num2 = int(input("Enter the second number (1st exponent): "))
            num3 = int(input("Enter the third number (2nd exponent): "))
        except ValueError:
            print("Invalid input! Please enter valid integers.\n")
            continue

        result = make_power(num1, num2, num3)
        print(f"\nResult: ({num1} ** {num2}) ** {num3} = {result}")
        print("-" * 50)

        query = input("Do you want to try again? (y/n): ").strip().lower()
        if query != "y":
            print("Exiting the program... Goodbye!\n")
            break


if __name__ == "__main__":
    main()
