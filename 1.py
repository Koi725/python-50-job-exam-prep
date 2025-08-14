"""
Description:
This program takes a two-digit integer from the user and calculates
the sum of its digits. The program validates input to ensure that
the entered value is indeed a two-digit number (positive or negative).
No frameworks, pure Python.
"""


def sum_of_digit(num: int) -> int:
    # absoulote number :
    abs_number = abs(num)

    # Extract the Units Digits s:
    units = abs_number % 10

    # tens the digits number :
    tens = abs_number // 10

    return units + tens


def main():
    """Main function to run the program."""
    try:
        user_input = int(input("pls enter the number : "))
        if not (10 <= user_input <= 99):
            print("Error! input must be two digits integer ")
            return

        result = sum_of_digit(user_input)

        print(f"Sum of digits : {result}")
    except ValueError:
        print("Error occured! pls enter the valid integer :")


if __name__ == "__main__":
    main()
