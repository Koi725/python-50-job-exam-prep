import random


def find_max(nums):
    max_val = nums[0]
    for num in nums[1:]:
        if num > max_val:
            max_val = num
    return max_val


def find_min(nums):
    min_val = nums[0]
    for num in nums[1:]:
        if num < min_val:
            min_val = num
    return min_val


def bubble_sort_desc(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def main():
    print("Manual Analysis of Random Numbers")

    while True:
        try:
            count = int(input("How many random numbers do you want? "))
            if count <= 0:
                print("❌ Number must be greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    numbers = [random.randint(1, 100000) for _ in range(count)]

    print("\nGenerated Numbers:")
    print(numbers)

    max_num = find_max(numbers)
    min_num = find_min(numbers)
    sorted_nums = bubble_sort_desc(numbers.copy())  # Use copy so original stays intact

    print("\nSorted Numbers (Descending):")
    print(sorted_nums)
    print(f"\nMax Number: {max_num}")
    print(f"Min Number: {min_num}")


if __name__ == "__main__":
    main()
