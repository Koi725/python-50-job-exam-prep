def diagonal_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)


def main():
    while True:
        try:
            num = int(input("Pls Enter The Number :"))
        except ValueError:
            print("Invalid Input..")
            continue
        diagonal_pattern(num)
        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()
