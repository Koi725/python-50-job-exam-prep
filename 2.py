def sum_of_numbers(num1, num2, num3):
    # Sum of 3 numberes :
    sum = num1 + num2 + num3
    # Average of 3 numbers :
    avg = num1 + num2 + num3 / 3

    print(f"The Sum is : {sum} and the average is : {avg}")


def main():
    for i in range(3):
        try:
            user_input = int(input(f"pls enter the number{i} :"))
        except ValueError:
            print("invalid integer type..!")


if __name__ == "__main":
    main()
