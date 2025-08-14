"""
Q05 — Area of a circle

Write a program that takes a number as the radius of a circle
and prints its area.
- Uses math.pi for higher precision.
- Rejects negative radii with a clear error message.
"""

from math import pi


def circle_area(radius: float) -> float:
    """
    Compute the area of a circle given its radius.

    Args:
        radius (float): Circle radius (must be >= 0)

    Returns:
        float: Area of the circle

    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return pi * (radius**2)


def main() -> None:
    while True:
        try:
            user_input = float(input("Please enter the radius: "))
            area = circle_area(user_input)
            print(f"Area of circle with radius {user_input} is: {area:.6f}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    main()
