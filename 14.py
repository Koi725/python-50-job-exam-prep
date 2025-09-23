def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def main():
    print("📘 Series Calculator: (2^i) / (2i+1)! for i = 0 to n-1\n")

    while True:
        try:
            n = int(input("Enter the number of terms (n): "))
            if n <= 0:
                print("Please enter a positive integer greater than 0.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.\n")
            continue

        total = 0.0

        for i in range(n):
            numerator = 2**i
            denominator = factorial(2 * i + 1)
            total += numerator / denominator

        print(f"\nResult of the series up to {n} terms: {total:.6f}")
        print("-" * 40)

        again = input("Do you want to try again? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting the program. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
