def diagonal_pattern(n):
    for i in range(1, n // 2 + 1):
        print("*" * i)
    for i in range(n // 2 - 1, 0, -1):
        print("*" * i)


def main():
    while True:
        try:
            num = int(input("Pls Enter The Number (Even Recommended) : "))
        except ValueError:
            print("Invalid Input. Please enter an integer.")
            continue

        diagonal_pattern(num)
        print("\n" + "-" * 40)

        q = input("Do you want to continue? (y/n): ")
        if q.lower() != "y":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
