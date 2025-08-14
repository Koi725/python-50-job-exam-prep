"""
Q06 — Roots of a quadratic equation

Write a program that reads the coefficients a, b, c (a ≠ 0) of a quadratic
equation ax^2 + bx + c = 0, computes the discriminant, and:

- If discriminant > 0: print the two distinct real roots.
- If discriminant == 0: print the (double) real root.
- If discriminant < 0: print "NO REAL ROOTS".

Notes:
- Input is read from stdin.
- Output is human-readable and consistent.
"""

from math import sqrt
from typing import Tuple, Optional


def discriminant(a: float, b: float, c: float) -> float:
    """Return the discriminant Δ = b^2 − 4ac."""
    return b * b - 4.0 * a * c


def solve_quadratic(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    Solve ax^2 + bx + c = 0 for real roots.

    Returns:
        (x1, x2) ordered with x1 >= x2 when real roots exist.
        None if there are no real roots.

    Raises:
        ValueError: if a == 0 (not a quadratic).
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must be non-zero for a quadratic equation.")

    d = discriminant(a, b, c)
    if d < 0:
        return None

    two_a = 2.0 * a
    if d == 0:
        x = -b / two_a
        return (x, x)

    sqrt_d = sqrt(d)
    x1 = (-b + sqrt_d) / two_a
    x2 = (-b - sqrt_d) / two_a
    # Ensure a consistent order (largest first)
    return (max(x1, x2), min(x1, x2))


def main() -> None:
    while True:
        try:
            a = float(input("Enter a (non-zero): ").strip())
            b = float(input("Enter b: ").strip())
            c = float(input("Enter c: ").strip())
            roots = solve_quadratic(a, b, c)

            if roots is None:
                print("NO REAL ROOTS")
            else:
                x1, x2 = roots
                if x1 == x2:
                    print(f"x = {x1:.6f}")
                else:
                    print(f"x1 = {x1:.6f}")
                    print(f"x2 = {x2:.6f}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    main()
