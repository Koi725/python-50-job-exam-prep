def make_power(base, exponent):
    """
    Calculates base raised to the power of exponent using a while loop.
    Does NOT use ** operator or any built-in power function.
    """
    if exponent == 0:
        return 1

    result = 1
    counter = 0

    while counter < exponent:
        result *= base
        counter += 1

    return result


def main():
    print("Power Calculator (using while loop only)\n")
    while True:
        try:
            num1 = int(input("Enter the base number: "))
            num2 = int(input("Enter the exponent: "))
        except ValueError:
            print("Invalid input. Please enter integers.\n")
            continue

        result = make_power(num1, num2)
        print(f"\n{num1} to the power of {num2} is: {result}")
        print("-" * 40)

        again = input("Do you want to continue? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting the program. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
