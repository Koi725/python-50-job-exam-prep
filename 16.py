def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def main():
    print("Series: 1 + 3²/3! - 5³/5! + 7⁴/7! - 9⁵/9! + ...")

    while True:
        try:
            n = int(input("Enter the number of terms (n ≥ 1): "))
            if n < 1:
                print("n must be at least 1.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.\n")
            continue

        total = 1

        for i in range(1, n):
            base = 2 * i + 1
            power = i + 1
            numerator = base**power
            denominator = factorial(base)
            sign = (-1) ** i
            term = sign * (numerator / denominator)
            total += term

        print(f"\nResult of the series with {n} terms: {total:.6f}")
        print("-" * 40)

        again = input("Try again? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
