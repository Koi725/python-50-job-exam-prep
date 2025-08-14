def sum_of_numbers(num1: float, num2: float, num3: float) -> None:
    """
    Calculate and print the sum and average of three numbers.

    Args:
        num1, num2, num3 (float): Input numbers
    """
    # Sum of the 3 numbers
    total_sum = num1 + num2 + num3

    # Average of the 3 numbers (correct precedence with parentheses)
    average = total_sum / 3

    print(f"The sum is: {total_sum} and the average is: {average}")


def main():
    """
    Main function to handle user input and call sum_of_numbers().
    """
    numbers = []

    for i in range(1, 4):  # Start from 1 for better UX
        while True:
            try:
                user_input = float(input(f"Please enter number {i}: "))
                numbers.append(user_input)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Unpack the list into the function
    sum_of_numbers(*numbers)


if __name__ == "__main__":
    main()
