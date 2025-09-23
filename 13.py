def main():
    print("📘 Series Calculator: (i / i!) from i = 1 to n\n")

    while True:
        try:
            n = int(input("👉 Enter a positive integer (n): "))
            if n <= 0:
                print("❌ Please enter a number greater than 0.\n")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter an integer.\n")
            continue

        i = 1
        fact = 1
        result = 0.0

        while i <= n:
            fact *= i  # calculate i!
            result += i / fact  # add i / i! to result
            i += 1

        print(f"\n✅ Result of the series up to n={n} is: {result:.6f}")
        print("-" * 40)

        again = input("🔁 Do you want to try another number? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Exiting the program. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
