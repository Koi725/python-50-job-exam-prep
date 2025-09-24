def factorial(num):
    res = 1
    for i in range(num):
        res *= num
    return res


def main():
    while True:
        try:
            n = int(input("Pls Enter The n number :"))
            if n <= 0:
                print("The Number Should Be Greater Than 0")
        except ValueError:
            print("Invalid Input...Pls Try Again")

        total = 0.0
        for i in range(n):
            numerator = (2 * i + 1) ** i
            denominator = factorial(2 * i + 1)
            total += numerator / denominator

        print(f"\nResult of the series up to {n} terms: {total:.2f}")
        print("-" * 40)

        again = input("Do you want to try again? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting the program. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
