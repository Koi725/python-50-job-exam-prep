"""
Q08 — Reverse or keep a three-digit number

Write a program that takes a three-digit integer from the user.
If the most significant digit (hundreds place) and the least significant digit (units place)
are equal, print the number itself; otherwise, print the reverse of the number.

Examples:
    Input: 171  → Output: 171
    Input: 325  → Output: 523
    Input: 989  → Output: 989
"""


def process_three_digit_number(n: int) -> int:
    """
    Process a three-digit number according to the problem statement.

    Args:
        n (int): A three-digit integer (±100..±999)

    Returns:
        int: Either the original number or its reverse.
    """
    abs_n = abs(n)
    if abs_n < 100 or abs_n > 999:
        raise ValueError("Input must be a three-digit integer (±100..±999).")

    first_digit = abs_n // 100
    last_digit = abs_n % 10

    if first_digit == last_digit:
        return n
    else:
        # Reverse the absolute number
        reversed_num = int(str(abs_n)[::-1])
        # Keep the sign of original number
        return reversed_num if n > 0 else -reversed_num


def main() -> None:
    while True:
        try:
            user_input = int(input("Enter a three-digit integer: ").strip())
            result = process_three_digit_number(user_input)
            print(f"Result: {result}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    main()
