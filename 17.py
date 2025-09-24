import random


def main():
    print("🎲 Random Number Analyzer")

    while True:
        try:
            n = int(input("How many random numbers do you want to generate? "))
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    numbers = [random.randint(1, 100000) for _ in range(n)]

    print("\nGenerated Numbers:")
    print(numbers)

    sorted_numbers = sorted(numbers, reverse=True)

    print("\nSorted (Descending):")
    print(sorted_numbers)

    print(f"\nMax number: {max(numbers)}")
    print(f"Min number: {min(numbers)}")


if __name__ == "__main__":
    main()
