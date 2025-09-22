def make_power(base, exponent):
    """
    Raises 'base' to the power of 'exponent' using a manual loop.
    Does NOT use the built-in '**' or 'pow()' for learning purposes.
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def main():
    print("⚡ Welcome to the Power Calculator App\n")

    while True:
        try:
            base = int(input("🔢 Enter the base number: "))
            exponent = int(input("🔢 Enter the exponent: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.\n")
            continue

        result = make_power(base, exponent)
        print(f"\n {base} raised to the power of {exponent} is: {result}")
        print("-" * 40)

        again = input(" Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("\n Exiting the program... See you!")
            break


if __name__ == "__main__":
    main()
